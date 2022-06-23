opcodes = {
    "events": {
        "on_flag": {
            "opcode": "event_whenflagclicked",
            "inputs": [

            ]
        },
        "on_key": {
            "opcode": "event_whenkeypressed",
            "inputs": [
                {
                    "type": "field",
                    "name": "KEY_OPTION"
                }
            ]
        },
        "on_click": {
            "opcode": "event_whenthisspriteclicked",
            "inputs": [

            ]
        },
        "on_background_switch": {
            "opcode": "event_whenbackdropswitchesto",
            "inputs": [
                {
                    "type": "field",
                    "name": "BACKDROP"
                }
            ]
        },
        "on_greater_than": {
            "opcode": "event_whengreaterthan",
            "inputs": [
                {
                    "type": "field",
                    "name": "WHENGREATERTHANMENU"
                },
                {
                    "type": "input",
                    "name": "NUMBER"
                }
            ]
        },
        "on_event": {
            "opcode": "event_whenbroadcastreceived",
            "inputs": [
                {
                    "type": "field",
                    "name": "BROADCAST_OPTION"
                }
            ]
        },
        "on_clone_start": {
            "opcode": "control_start_as_clone",
            "inputs": [

            ]
        }
    },
    "motion": {
        "move_steps": {
            "opcode": "motion_movesteps",
            "inputs": [
                {
                    "type": "input",
                    "name": "STEPS",
                }
            ]
        },
        "turn_right": {
            "opcode": "motion_turnright",
            "inputs": [
                {
                    "type": "input",
                    "name": "DEGREES",
                }
            ]
        },
        "turn_left": {
            "opcode": "motion_turnleft",
            "inputs": [
                {
                    "type": "input",
                    "name": "DEGREES",
                }
            ]
        },
        "go_to": {
            "opcode": "motion_goto",
            "inputs": [
                {
                    "type": "shadow",
                    "name": "TO",  # Shadow
                    "shadow": "shadow.gotomenu"
                }
            ]
        },

        "set_position": {
            "opcode": "motion_gotoxy",
            "inputs": [
                {
                    "type": "input",
                    "name": "X",
                },
                {
                    "type": "input",
                    "name": "Y",
                }
            ]
        },

        "glide_to": {
            "opcode": "motion_glideto",
            "inputs": [
                {
                    "type": "input",
                    "name": "SECS"
                },
                {
                    "type": "shadow",
                    "name": "TO",  # Shadow
                    "shadow": "shadow.glidetomenu"
                }
            ]
        },

        "glide_to_pos": {
            "opcode": "motion_glidesecstoxy",
            "inputs": [
                {
                    "type": "input",
                    "name": "SECS"
                },
                {
                    "type": "input",
                    "name": "X"
                },
                {
                    "type": "input",
                    "name": "Y"
                }
            ]
        },

        "point_in_direction": {
            "opcode": "motion_pointindirection",
            "inputs": [
                {
                    "type": "input",
                    "name": "DIRECTION"
                }
            ]
        },

        "point_towards": {
            "opcode": "motion_pointtowards",
            "inputs": [
                {
                    "type": "shadow",
                    "name": "TOWARDS",  # Shadow
                    "shadow": "shadow.pointtowardsmenu"
                }
            ]
        },

        "change_x": {
            "opcode": "motion_changexby",
            "inputs": [
                {
                    "type": "input",
                    "name": "DX"
                }
            ]
        },

        "set_x": {
            "opcode": "motion_setx",
            "inputs": [
                {
                    "type": "input",
                    "name": "X"
                }
            ]
        },

        "change_y": {
            "opcode": "motion_changeyby",
            "inputs": [
                {
                    "type": "input",
                    "name": "DY"
                }
            ]
        },

        "set_y": {
            "opcode": "motion_sety",
            "inputs": [
                {
                    "type": "input",
                    "name": "Y"
                }
            ]
        },

        "set_rot_style": {
            "opcode": "motion_setrotationstyle",
            "inputs": [
                {
                    "type": "field",
                    "name": "STYLE"
                }
            ]
        },

        "shadows": {
            "shadow.gotomenu": {
                "opcode": "motion_gotomenu",
                "inputs": [
                    {
                        "type": "field",
                        "name": "TO"
                    }
                ]
            },
            "shadow.glidetomenu": {
                "opcode": "motion_glideto_menu",
                "inputs": [
                    {
                        "type": "field",
                        "name": "TO"
                    }
                ]
            },
            "shadow.pointtowardsmenu": {
                "opcode": "motion_pointtowards_menu",
                "inputs": [
                    {
                        "type": "field",
                        "name": "TOWARDS"
                    }
                ]
            }
        }
    },

    "looks": {
        "timed_say": {
            "opcode": "looks_sayforsecs",
            "inputs": [
                {
                    "type": "input",
                    "name": "MESSAGE"
                },
                {
                    "type": "input",
                    "name": "SECS"
                }
            ]
        },
        "say": {
            "opcode": "looks_say",
            "inputs": [
                {
                    "type": "input",
                    "name": "MESSAGE"
                }
            ]
        },
        "timed_think": {
            "opcode": "looks_thinkforsecs",
            "inputs": [
                {
                    "type": "input",
                    "name": "MESSAGE"
                },
                {
                    "type": "input",
                    "name": "SECS"
                }
            ]
        },
        "think": {
            "opcode": "looks_think",
            "inputs": [
                {
                    "type": "input",
                    "name": "MESSAGE"
                }
            ]
        },
        "set_costume": {
            "opcode": "ember_override_function",
            "override": None,  # TODO: Implement function overrides
            "inputs": [
                {
                    "type": "shadow",
                    "name": "COSTUME",  # Shadow
                    "shadow": "shadow.costume"
                }
            ]
        },
        "advance_costume": {
            "opcode": "looks_nextcostume",
            "inputs": [

            ]
        },

        "set_backdrop": {
            "opcode": "ember_override_function",
            "override": None,  # TODO: Implement function overrides
            "inputs": [
                {
                    "type": "shadow",
                    "name": "BACKDROP",  # Shadow
                    "shadow": "shadow.backdrop"
                }
            ]
        },

        "change_size": {
            "opcode": "looks_changesizeby",
            "inputs": [
                {
                    "type": "input",
                    "name": "CHANGE"
                }
            ]
        },

        "set_size": {
            "opcode": "looks_setsizeto",
            "inputs": [
                {
                    "type": "input",
                    "name": "SIZE"
                }
            ]
        },

        "change_effect": {
            "opcode": "looks_changeeffectby",
            "inputs": [
                {
                    "type": "input",
                    "name": "CHANGE"
                },
                {
                    "type": "field",
                    "name": "EFFECT"
                }
            ]
        },

        "set_effect": {
            "opcode": "looks_seteffectto",
            "inputs": [
                {
                    "type": "input",
                    "name": "VALUE"
                },
                {
                    "type": "field",
                    "name": "EFFECT"
                }
            ]
        },

        "clear_effects": {
            "opcode": "looks_cleargraphiceffects",
            "inputs": [

            ]
        },

        "show": {
            "opcode": "looks_show",
            "inputs": [

            ]
        },

        "hide": {
            "opcode": "looks_hide",
            "inputs": [

            ]
        },

        "go_to_front_back": {
            "opcode": "looks_gotofrontback",
            "inputs": [
                {
                    "type": "field",
                    "name": "FRONT_BACK"
                }
            ]
        },

        "change_layer": {
            "opcode": "looks_goforwardbackwardlayers",
            "inputs": [
                {
                    "type": "field",
                    "name": "FORWARD_BACKWARD"
                },
                {
                    "type": "input",
                    "name": "NUM"
                }
            ]
        },

        "shadows": {
            "shadow.costume": {
                "opcode": "looks_costume",
                "inputs": [
                    {
                        "type": "field",
                        "name": "COSTUME"
                    }
                ]
            },
            "shadow.backdrop": {
                "opcode": "looks_backdrops",
                "inputs": [
                    {
                        "type": "field",
                        "name": "BACKDROP"
                    }
                ]
            }
        }

    },

    "sound": {
        "play_sound_until_done": {
            "opcode": "sound_playuntildone",
            "inputs": [
                {
                    "type": "shadow",
                    "name": "SOUND_MENU",  # Shadow
                    "shadow": "shadow.sound_menu"
                }
            ]
        },

        "play_sound": {
            "opcode": "sound_play",
            "inputs": [
                {
                    "type": "shadow",
                    "name": "SOUND_MENU",  # Shadow
                    "shadow": "shadow.sound_menu"
                }
            ]
        },

        "stop_sounds": {
            "opcode": "sound_stopallsounds",
            "inputs": [

            ]
        },

        "change_sound_effect": {
            "opcode": "sound_changeeffectby",
            "inputs": [
                {
                    "type": "field",
                    "name": "EFFECT"
                },
                {
                    "type": "input",
                    "name": "VALUE"
                }
            ]
        },

        "set_sound_effect": {
            "opcode": "sound_seteffectto",
            "inputs": [
                {
                    "type": "field",
                    "name": "EFFECT"
                },
                {
                    "type": "input",
                    "name": "VALUE"
                }
            ]
        },

        "clear_sound_effects": {
            "opcode": "sound_cleareffects",
            "inputs": [

            ]
        },

        "change_volume": {
            "opcode": "sound_changevolumeby",
            "inputs": [
                {
                    "type": "input",
                    "name": "VOLUME",
                }
            ]
        },

        "set_volume": {
            "opcode": "sound_setvolumeto",
            "inputs": [
                {
                    "type": "input",
                    "name": "VOLUME",
                }
            ]
        },

        "shadows": {
            "shadow.sound_menu": {
                "opcode": "sound_sounds_menu",
                "inputs": [
                    {
                        "type": "field",
                        "name": "SOUND_MENU"
                    }
                ]
            }
        }
    },

    "control": {
        "wait": {
            "opcode": "control_wait",
            "inputs": [
                {
                    "type": "input",
                    "name": "DURATION"
                }
            ]
        }
    },

    "sensing": {
        "ask": {
            "opcode": "sensing_askandwait",
            "inputs": [
                {
                    "type": "input",
                    "name": "QUESTION"
                }
            ]
        },
        "set_drag_mode": {
            "opcode": "sensing_setdragmode",
            "inputs": [
                {
                    "type": "field",
                    "name": "DRAG_MODE"
                }
            ]
        },
        "reset_timer": {
            "opcode": "sensing_resettimer",
            "inputs": [

            ]
        }
    },

    "operators": {

    },

    "variables": {
        "show_variable": {
            "opcode": "data_showvariable",
            "inputs": [
                {
                    "type": "field",
                    "name": "VARIABLE"
                }
            ]
        },
        "hide_variable": {
            "opcode": "data_hidevariable",
            "inputs": [
                {
                    "type": "field",
                    "name": "VARIABLE"
                }
            ]
        }
    },

    "lists": {
        "show_list": {
            "opcode": "data_showlist",
            "inputs": [
                {
                    "type": "field",
                    "name": "LIST"
                }
            ]
        },
        "hide_list": {
            "opcode": "data_hidelist",
            "inputs": [
                {
                    "type": "field",
                    "name": "LIST"
                }
            ]
        }
    }
}

# TODO: Complete for every field


# Outputs whether the field is valid and if it is referencing an object
def filter_fields(field, value, current, backdrop, sprites):

    active = [current, backdrop]
    objects = sprites + active

    match field:
        case "KEY_OPTION":
            if value.isalpha() or value.isdigit() or value in ["any", "space", "up arrow", "left arrow", "down arrow", "right arrow"]:
                return value, None

        case "BACKDROP":
            for costume in backdrop.costumes:
                if costume.name == value:
                    return value, None

        case "WHENGREATERTHANMENU":
            if value.lower() in ["loudness", "timer"]:
                return value.upper(), None

        case "BROADCAST_OPTION":
            for obj in objects:
                for broadcast in obj.broadcasts:
                    if broadcast.name == value:
                        return value, None

        case "VARIABLE":
            for obj in active:
                for var in obj.variables:
                    if var.name == value:
                        return value, var.id

        case "LIST":
            for obj in active:
                for lst in obj.lists:
                    if lst.name == value:
                        return value, lst.id

        case "EFFECT":
            if value.lower() in ["color", "fisheye", "whirl", "pixelate", "mosaic"]:
                return value.upper(), None
            elif value.lower() in ["pitch", "pan"]:
                return value.upper(), None

        case "STYLE":
            if value.lower() in ["left-right", "all-around", "no-rotate"]:
                if value == "all-around":
                    return "all around", None
                elif value == "no-rotate":
                    return "don't rotate", None
                else:
                    return value, None

        case "FRONT_BACK":
            if value.lower() in ["front", "back"]:
                return value.lower(), None

        case "FORWARD_BACKWARD":
            if value.lower() in ["forward", "backward"]:
                return value.lower(), None

        case "TO":
            if value in ["random", "mouse"]:
                return f"_{value}_", None

        case "TOWARDS":
            if value in ["mouse"]:
                return f"_{value}_", None

        case "BROADCAST_OPTION":
            for obj in objects:
                if value == obj.name:
                    return obj.name, obj.id

        case "DRAG_MODE":
            if value in ["draggable", "not_draggable"]:
                return value.replace("_", " "), None

    return None, None


# TODO: Filter for inputs
