# Data used in the language and to assemble the json
# Each has a json_constructor function

import hashlib
import shutil
import os

id = 0

class Stage:
    def __init__(self):
        self.name = 'Stage'
        self.variables = []
        self.lists = []
        self.broadcasts = []
        self.blocks = []
        self.costumes = []
        self.sounds = []
        self.currentCostume = 0
        self.volume = 100
        self.tempo = 60
        self.layerOrder = 0
        self.videoTransparency = 50
        self.videoState = 'on'
        self.textToSpeechLanguage = None

    def json_constructor(self):
        return {
            "isStage": True,
            "name": self.name,
            "variables": {
                variable.id: variable.json_constructor() for variable in self.variables
            },
            "lists": {},
            "broadcasts": {
                broadcast.id: broadcast.json_constructor() for broadcast in self.broadcasts
            },
            "costumes": [
                {
                    "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                    "name": "costume1",
                    "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                    "dataFormat": "svg",
                    "rotationCenterX": 240,
                    "rotationCenterY": 180
                }
            ] if len(self.costumes) == 0 else [costume.json_constructor() for costume in self.costumes],
            "sounds": [],
            "comments": {},
            "blocks": {
                block.id: block.json_constructor() for block in self.blocks
            },
            "currentCostume": self.currentCostume,
            "volume": 100,
            "layerOrder": self.layerOrder,
            "tempo": self.tempo,
            "videoTransparency": self.videoTransparency,
            "videoState": self.videoState,
            "textToSpeechLanguage": self.textToSpeechLanguage
        }

class Sprite:
    def __init__(self, name):
        self.name = name
        self.variables = []
        self.lists = []
        self.broadcasts = []
        self.blocks = []
        self.costumes = []
        self.sounds = []
        self.currentCostume = 0
        self.volume = 100
        self.visible = True
        self.x = 0
        self.y = 0
        self.size = 100
        self.direction = 90
        self.draggle = False
        self.rotationStyle = 'all around'

    def json_constructor(self, sprites):
        return {
            "isStage": False,
            "name": self.name,
            "variables": {
                variable.id: variable.json_constructor() for variable in self.variables
            },
            "lists": {},
            "broadcasts": {
                broadcast.id: broadcast.json_constructor() for broadcast in self.broadcasts
            },
            "blocks": {
                block.id: block.json_constructor() for block in self.blocks
            },
            "costumes": [
                {
                    "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                    "name": "costume1",
                    "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                    "dataFormat": "svg",
                    "rotationCenterX": 240,
                    "rotationCenterY": 180
                }
            ] if len(self.costumes) == 0 else [costume.json_constructor() for costume in self.costumes],
            "sounds": [],
            "comments": {},
            "currentCostume": self.currentCostume,
            "volume": self.volume,
            "layerOrder": sprites.index(self) + 1,
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "direction": self.direction,
            "draggle": self.draggle,
            "rotationStyle": self.rotationStyle
        }
        
class Variable:
    def __init__(self, name, value, id):
        self.name = name
        self.value = value
        self.id = id

    def json_constructor(self):
        return [
            self.name,
            self.value
        ]

class List:
    pass # TODO:

class Broadcast:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def json_constructor(self):
        return self.name
        

class Costume:
    def __init__(self, path):
        self.path = path
        self.assetId = self.generate_md5()
        self.name = path.split('/')[-1].split('.')[0]
        self.dataFormat = path.split('/')[-1].split('.')[1]
        self.md5ext = self.generate_md5() + '.' + self.dataFormat
        self.rotationCenterX = 0
        self.rotationCenterY = 0

        if os.path.getsize(path) > (10 * (1024 ** 2)):
            print(f"[WARN] File \"{self.name}.{self.dataFormat}\" is too big for the scratch website")

    def generate_md5(self):
        with open(self.path, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()

        return md5

    def save_file(self, out):
        shutil.copyfile(self.path, f'{out}/{self.md5ext}')

    def json_constructor(self):
        return {
            "assetId": self.assetId,
            "name": self.name,
            "md5ext": self.md5ext,
            "dataFormat": self.dataFormat,
            "rotationCenterX": self.rotationCenterX,
            "rotationCenterY": self.rotationCenterY
        }

class Sound:
    def __init__(self, path):
        self.path = path
        self.assetId = self.generate_md5(),
        self.name = path.split('/')[-1].split('.')[0]
        self.dataFormat = path.split('/')[-1].split('.')[1]
        self.md5ext = self.generate_md5() + '.' + self.dataFormat
        self.format = ""
        self.rate = 48000
        self.sampleCount = 1124

        if os.path.getsize(path) > (10 * (1024 ** 2)):
            print(f"[WARN] File \"{self.name}.{self.dataFormat}\" is too big for the scratch website")

    def generate_md5(self):
        with open(self.path, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()

        return md5
        


    def json_constructor(self):
        return {
            "assetId": self.assetId,
            "name": self.name,
            "dataFormat": self.dataFormat,
            "format": self.format,
            "rate": self.rate,
            "sampleCount": self.sampleCount,
            "md5ext": self.md5ext
        }


class Project:
    def __init__(self, stage, sprites):
        self.stage = stage
        self.sprites = sprites

    def json_constructor(self):
        return {
            "targets": [
                self.stage.json_constructor(),
                *[sprite.json_constructor(self.sprites) for sprite in self.sprites]
            ],
            "monitors": [],
            "extensions": [],
            "meta": {
                "semver": "3.0.0",
                "vm": "0.2.0-prerelease.20220510130158",
                "agent": "Created with Ember by -EmeraldThunder-"
            }
        }

class Block:
    def __init__(self, opcode, id):
        self.opcode = opcode
        self.next = None
        self.parent = None
        self.inputs = {}
        self.fields = {}
        self.shadow = False
        self.x = 0
        self.y = 0
        self.id = id

    def json_constructor(self):
        return {
            "opcode": self.opcode,
            "next": str(self.next) if self.next != None else self.next,
            "parent": str(self.parent) if self.parent != None else self.parent,
            "inputs": {
                _input.name: _input.json_constructor() for _input in self.inputs
            },
            "fields": {
                field.name: field.json_constructor() for field in self.fields
            },
            "shadow": self.shadow,
            "topLevel": True if self.parent == None else False,
            "x": self.x,
            "y": self.y
        }

class Field:
    def __init__(self, name, value, links):
        self.name = name
        self.value = value
        self.links = links

    def json_constructor(self):
        return [
            self.value,
            self.links
        ]

class InputRaw:
    def __init__(self, value, _type, isShadow, dataType):
        self.value = value
        self.type = _type
        self.isShadow = isShadow
        self.dataType = dataType

class Input():
    def __init__(self,  name, values):
        self.name = name
        self.values = values # List of InputRaw objects in the order they are in the block

        self.i_type = None

        if self.value[-1].type == "shadow":
            self.i_type = 1
        elif "shadow" in [i.value for i in self.value]:
            self.i_type = 3
        else:
            self.i_type = 2
        
def new_id():
    global id

    id += 1
    return id