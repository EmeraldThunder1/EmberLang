import json

from src.tokens import *
from src.errors import *
from src.defaultData import *
from src.opcodes import *
        
class Compiler:
    def __init__(self, out):
        self.idx = 0
        self.tokens = None
        self.out = out
        self.id = 0

        self.reachedEnd = lambda : False if self.idx < len(self.tokens) else True
        self.isStackOpen = lambda : True if 'event' in self.scope_stack else False

    def compile(self, tokens):
        self.idx = 0
        self.tokens = tokens

        sprites = []

        self.scope_stack = []

        current_sprite = None
        backdrop = None

        while self.idx < len(self.tokens):
            if self.tokens[self.idx].type == IDENTIFIER:
                if self.tokens[self.idx].value == "Stage":
                    self.idx += 1

                    if not self.reachedEnd():
                        if self.tokens[self.idx].type == IDENTIFIER:
                            raise(NamingError("Object of type stage cannot have a name"))

                        else:
                            if not backdrop:
                                backdrop = Stage()
                                self.scope_stack.append('stage')

                                if not self.tokens[self.idx].type == OPEN_BRACE:
                                    raise(SyntaxError("Expected '{' after stage declaration"))

                                self.idx += 1
                            else:
                                raise(DeclarationError("Cannot create two stages"))

                elif self.tokens[self.idx].value == "Sprite":
                    self.idx += 1
                    
                    if not self.reachedEnd():
                        if self.tokens[self.idx].type == IDENTIFIER:
                            sprite_name = self.tokens[self.idx].value
                            
                            self.scope_stack.append('sprite')
                            current_sprite = Sprite(sprite_name)

                            self.idx += 1

                            if not self.tokens[self.idx].type == OPEN_BRACE:
                                    raise(SyntaxError("Expected '{' after sprite declaration"))

                            self.idx += 1

                elif self.tokens[self.idx].value in ["var", "global"]:
                    var_type = self.tokens[self.idx].value

                    self.idx += 1

                    if not self.reachedEnd():
                        if self.tokens[self.idx].type == IDENTIFIER:
                            var_name = self.tokens[self.idx].value
                            var_value = None

                            self.idx += 1

                            if not self.reachedEnd():
                                if self.tokens[self.idx].type == ASSIGNMENT:
                                    self.idx += 1

                                    if not self.reachedEnd():
                                        if self.tokens[self.idx].type in [STRING, NUMBER, BOOLEAN, NULL]:
                                                var_value = self.tokens[self.idx].value

                                        else:
                                            raise SyntaxError("Expected data after assignment")
                                    else:
                                        raise SyntaxError("Expected data after assignment")

                                    self.idx += 1

                            variable = Variable(var_name, var_value, self.next_id())
                            

                            if var_type == "var":
                                if not self.scope_stack[-1] == 'stage':
                                    if current_sprite:
                                        current_sprite.variables.append(variable)
                                    else:
                                        raise DeclarationError("Cannot declare local variable outside of a sprite")
                                else:
                                    raise DeclarationError("Cannot declare a local variable in the stage")

                            elif var_type == "global":
                                if backdrop:
                                    backdrop.variables.append(variable)
                                else:
                                    raise DeclarationError("A stage must be defined to declare globals")


                    else:
                        raise(SyntaxError("Expected variable name"))

                elif self.tokens[self.idx].value == "set_costume":
                    self.idx += 1

                    if not self.reachedEnd():
                        params = self.parse_parameters()

                        if not len(params) == 1:
                            raise SyntaxError("Function set costume expects one parameter")

                        img_file = params[0].value

                        costume = Costume(img_file)

                        if self.get_last_object() == 'stage':
                            costume.save_file(self.out)
                            backdrop.costumes.append(costume)
                        elif current_sprite:
                            costume.save_file(self.out)
                            current_sprite.costumes.append(costume)

                        # Create block that sets the costume and append it onto event stack
 
                        block = Block('looks_switchcostumeto', self.next_id())
                        if self.get_last_object() == 'stage':
                            prev_block = backdrop.blocks[-1]
                        else:
                            prev_block = current_sprite.blocks[-1]

                        prev_block.next = block.id
                        block.parent = prev_block.id

                        if self.get_last_object() == 'stage':
                            backdrop.blocks.append(block)
                        else:
                            current_sprite.blocks.append(block)
                
                else:
                    # Command is being called
                    name = self.tokens[self.idx].value

                    command = None

                    for category in opcodes.values():
                        for key in category.keys():
                            if name == key and (not key in ['shadows']):
                                command = category[key]
                                break

                        if command != None:
                            break

                    if command == None:
                        raise UndefinedError(f"The function {name} has not been found in the ember library or any addon")
                        # TODO: Similar commands

                    self.idx += 1
                    self.parse_parameters()
                    
                    if command['opcode'] != "ember_override_function":
                        block = Block(command['opcode'], self.next_id())

                        prev_block_next = block.id

                        if self.get_last_object() != 'stage':
                            parent_id = current_sprite.blocks[-1].id
                        else:
                            parent_id = backdrop.blocks[-1].id

                        if self.get_last_object() != 'stage':
                            prev_block = current_sprite.blocks[-1]
                        else:
                            prev_block = backdrop.blocks[-1]

                        prev_block.next = prev_block_next


                        block.parent = parent_id

                        if self.get_last_object() == 'stage':
                            backdrop.blocks.append(block)
                        else:
                            current_sprite.blocks.append(block)


                    
                # TODO: Attach block to stack to set variable                    


            elif self.tokens[self.idx].type == CLOSE_BRACE:
                if self.scope_stack[-1] == 'sprite':
                    if current_sprite:
                        sprites.append(current_sprite)
                        current_sprite = None

                self.scope_stack.pop(-1)

                self.idx += 1

            elif self.tokens[self.idx].type == AT:
                self.idx += 1
                if not self.reachedEnd():
                    if self.tokens[self.idx].type == IDENTIFIER:
                        event_name = self.tokens[self.idx].value

                        self.idx += 1

                        if not self.reachedEnd():
                            event_params = self.parse_parameters()


                            if not self.reachedEnd():
                                if self.tokens[self.idx].type == OPEN_BRACE:
                                    self.idx += 1
                                    self.scope_stack.append('event')

                                else:
                                    raise SyntaxError("Expected '{' after event handler")


                        block = Block(opcodes['events'][event_name]['opcode'], self.next_id())

                        if current_sprite:
                            current_sprite.blocks.append(block)
                        elif 'stage' in self.scope_stack:
                            backdrop.blocks.append(block)
                        else:
                            raise ScopeError("Event must be associated with object")
                                    
        # Assemble the project.json and save any assets to the project folder. Zip it to .sb3 and store in "out"
        #TODO: Zip folder
        project = Project(backdrop, sprites)
        project_json = project.json_constructor()

        with open(f'{self.out}/project.json', 'w') as f:
            f.write(json.dumps(project_json, indent=4))

        if os.path.getsize(f'{self.out}/project.json') > 5 * (1024 ** 2):
            print("[WARN] The project.json file is too big to be uploaded to the scratch website")

        print(self.scope_stack)
            


    def next_id(self):
        self.id += 1
        return self.id

    def parse_parameters(self):
        if self.tokens[self.idx].type == OPEN_PAREN:
            self.idx += 1

            params = []

            prev = True
            while self.tokens[self.idx].type != CLOSE_PAREN:
                if self.reachedEnd():
                    raise SyntaxError("Unclosed parentheses")

                if prev:
                    param = self.tokens[self.idx]
                    prev = not prev

                    params.append(param)
                else:
                    if not self.tokens[self.idx].type in [COMMA, CLOSE_PAREN]:
                        raise SyntaxError("Parameters must be comma seperated values")

                    prev = not prev

                self.idx += 1

            self.idx += 1

        return params

    def get_last_object(self, _id=False):
        try:
            id = -1

            while not self.scope_stack[id] in ['stage', 'sprite']:
                id -= 1
            
            if _id:
                return id
            else:
                return self.scope_stack[id]
        
        except IndexError:
            return None

        