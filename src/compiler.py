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

        self.spirtes = []

        self.scope_stack = []

        self.scope = 0

        self.current_sprite = None
        self.backdrop = None

        self.closed = None

        while self.idx < len(self.tokens):
            if self.tokens[self.idx].type == IDENTIFIER:
                if self.tokens[self.idx].value == "Stage":
                    self.idx += 1

                    if not self.reachedEnd():
                        if self.tokens[self.idx].type == IDENTIFIER:
                            raise(NamingError("Object of type stage cannot have a name"))

                        else:
                            if not self.backdrop:
                                self.backdrop = Stage()
                                self.scope_stack.append('stage')

                                if not self.tokens[self.idx].type == OPEN_BRACE:
                                    raise(SyntaxError("Expected '{' after stage declaration"))
                                self.scope += 1

                                self.idx += 1
                            else:
                                raise(DeclarationError("Cannot create two stages"))

                elif self.tokens[self.idx].value == "Sprite":
                    self.idx += 1
                    
                    if not self.reachedEnd():
                        if self.tokens[self.idx].type == IDENTIFIER:
                            sprite_name = self.tokens[self.idx].value
                            
                            self.scope_stack.append('sprite')
                            self.current_sprite = Sprite(sprite_name)

                            self.idx += 1

                            if not self.tokens[self.idx].type == OPEN_BRACE:
                                    raise(SyntaxError("Expected '{' after sprite declaration"))

                            self.idx += 1
                            self.scope += 1

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
                                    if self.current_sprite:
                                        self.current_sprite.variables.append(variable)
                                    else:
                                        raise DeclarationError("Cannot declare local variable outside of a sprite")
                                else:
                                    raise DeclarationError("Cannot declare a local variable in the stage")

                            elif var_type == "global":
                                if self.backdrop:
                                    self.backdrop.variables.append(variable)
                                else:
                                    raise DeclarationError("A stage must be defined to declare globals")


                    else:
                        raise(SyntaxError("Expected variable name"))   
                else:
                    # TODO: Check if the name is a variable
                    # Command is being called
                    name = self.tokens[self.idx].value

                    command = None

                    # TODO: Handle it seperatly if c block is used

                    for category in opcodes.keys():
                        for key in opcodes[category].keys():
                            if name == key and (not key in ['shadows', 'c']):
                                command = opcodes[category][key]

                                command_inputs = command['inputs']
                                block_category = category

                                break

                        if command != None:
                            break

                    if command == None:
                        raise UndefinedError(f"The function {name} has not been found in the ember library or any addon")
                        # TODO: Similar commands

                    self.idx += 1

                        # Add the result / uses to a list

                    params = self.parse_parameters()

                    if command['opcode'] == 'ember_override_function':
                        if command['override'] == 'set_costume':
                            command['opcode'] = "looks_switchcostumeto"

                            file = params[0]
                            params[0] = Token(STRING, file.value.split('.')[0].split('/')[-1])

                            costume = Costume(file.value)

                            if self.get_last_object == 'stage':
                                self.backdrop.costumes.append(costume)
                            else:
                                self.current_sprite.costumes.append(costume)

                    block = Block(command['opcode'], self.next_id(), False, self.scope)

                    fields, inputs = self.filter_params(params, command_inputs, block, block_category)

                    if block_category == 'c_blocks':
                        block.c = True
                        raw = InputRaw(None, 'SUBSTACK', SUBSTACK, True, True)
                        _i = Input('SUBSTACK', raw)

                        inputs.append(_i)
                        
                        if self.tokens[self.idx].type == OPEN_BRACE:
                            self.scope += 1
                            self.scope_stack.append(str(block.id))
                            self.idx += 1
                        else:
                            raise SyntaxError(f'Expected open brace for the {name} block')

                    block.inputs += inputs
                    block.fields += fields

                    self.append_block(block)


                    
                # TODO: Attach block to stack to set variable                    


            elif self.tokens[self.idx].type == CLOSE_BRACE:
                if self.scope_stack[-1] == 'sprite':
                    if self.current_sprite:
                        self.spirtes.append(self.current_sprite)
                        self.current_sprite = None

                self.scope -= 1

                if self.scope_stack[-1].isdigit():
                    block = None
                    
                    if self.get_last_object() == 'stage':
                        active = self.backdrop
                    else:
                        active = self.current_sprite

                    for i in range(len(active.blocks)):
                        if active.blocks[i].id == int(self.scope_stack[-1]):
                            block = active.blocks.pop(i)
                            active.blocks.append(block)


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

                            # TODO: Filter


                            if not self.reachedEnd():
                                if self.tokens[self.idx].type == OPEN_BRACE:
                                    self.scope += 1
                                    self.idx += 1
                                    self.scope_stack.append('event')

                                else:
                                    raise SyntaxError("Expected '{' after event handler")


                        block = Block(opcodes['events'][event_name]['opcode'], self.next_id(), False, self.scope)

                        if self.current_sprite:
                            self.current_sprite.blocks.append(block)
                        elif 'stage' in self.scope_stack:
                            self.backdrop.blocks.append(block)
                        else:
                            raise ScopeError("Event must be associated with object")
                                    
        # Assemble the project.json and save any assets to the project folder. Zip it to .sb3 and store in "out"
        #TODO: Zip folder
        project = Project(self.backdrop, self.spirtes)
        project_json = project.json_constructor()

        with open(f'{self.out}/project.json', 'w') as f:
            f.write(json.dumps(project_json, indent=4))

        if os.path.getsize(f'{self.out}/project.json') > 5 * (1024 ** 2):
            print("[WARN] The project.json file is too big to be uploaded to the scratch website")            


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

    def filter_params(self, params, expected, block, category='events'):
        if len(params) != len(expected):
            raise ParameterError(f"Expected {str(len(expected))} parameters; got {str(len(params))} instead")

        fields = []
        inputs = []   

        for i in range(len(expected)):
            param = params[i]

            if expected[i]['type'] == "field":
                result, uses = filter_fields(expected[i]['name'], param, self.current_sprite, self.backdrop, self.spirtes)

                if result is None:
                    raise ParameterError(f"Unexpected value ({param}) for parameter of type {expected[i]['name']}")

                field = Field(expected[i]['name'], result.value, uses)
                fields.append(field)

            elif expected[i]['type'] == "input":
                result = filter_inputs(expected[i]['name'], param, self.current_sprite, self.backdrop, self.spirtes)

                if result is None:
                    raise ParameterError(f"Unexpected value ({param}) for parameter of type {expected[i]['name']}")

                raw_input = InputRaw(result.value, result.type, expected[i]['name'], False)
                _input = Input(expected[i]['name'], raw_input)

                inputs.append(_input)
                
            else:
                shadow_id = expected[i]['shadow']
                shadow_data = opcodes[category]['shadows'][shadow_id]

                shadow = Block(shadow_data['opcode'], self.next_id(), False, self.scope)
                shadow.shadow = True

                shadow_input = shadow_data['inputs'][0]

                result, uses = filter_fields(shadow_input['name'], param, self.current_sprite, self.backdrop, self.spirtes)

                if result is None:
                    raise ParameterError(f"Unexpected value ({param}) for parameter of type {shadow_input['name']}")
                
                field = Field(shadow_input['name'], result.value, uses)
                shadow.fields.append(field)

                shadow.parent = block.id

                if self.get_last_object() == 'stage':
                    self.backdrop.shadows.append(shadow)
                else:
                    self.current_sprite.shadows.append(shadow)

                raw_input = InputRaw(shadow.id, SHADOW, shadow_input['name'], True)
                _input = Input(shadow_input['name'], raw_input)

                inputs.append(_input)

        return fields, inputs

    def append_block(self, block):
        if self.get_last_object() != 'stage':
            prev_block = self.current_sprite.blocks[-1]
        else:
            prev_block = self.backdrop.blocks[-1]

        if prev_block.c:
            substack = None

            for i in prev_block.inputs:
                if i.name == "SUBSTACK":
                    substack = i
                    break

            substack.component2 = self.id

        block.parent = prev_block.id

        if not prev_block.c:
            prev_block.next = block.id
        else:
            if self.scope == block.scope:
                prev_block.next = block.id
        
        if self.get_last_object() == 'stage':
            self.backdrop.blocks.append(block)
        else:
            self.current_sprite.blocks.append(block)

        