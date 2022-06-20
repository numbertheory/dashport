#!/usr/bin/env python3

import curses


def color_names(color_backgrounds=None):
    color_constants = {"default": -1, "black": 0, "maroon": 1, "green": 2,
                       "olive": 3, "navy": 4, "purple": 5, "teal": 6,
                       "silver": 7, "grey": 8, "red": 9, "lime": 10,
                       "yellow": 11, "blue": 12, "fuchsia": 13, "aqua": 14,
                       "white": 15}
    if isinstance(color_backgrounds, list):
        try:
            color_backgrounds = {x: color_constants[x] for x in color_backgrounds}
        except KeyError:
            print(f"One or more colors listed not supported: {color_backgrounds}")
    else:
        color_backgrounds = {"default": -1, "white": 15,
                             "black": 0, "silver": 7, "grey": 8,
                             "red": 9, "lime": 10, "yellow": 11,
                             "blue": 12, "fuchsia": 13, "aqua": 14,
                             "maroon": 1, "green": 2, "navy": 4, "purple": 5}
    color_index = 1
    color_dict = dict()
    for name in list(color_backgrounds.keys()):
        for k in range(-1, 16):
            color_dict = color_foregrounds(color_index, color_backgrounds[name], color_dict, name)
        color_index += 17
    return color_dict, color_backgrounds


def color_foregrounds(color_index, color_int_background, color_dict, color_str_background):
    color_str = ["default", "black", "maroon", "green", "olive", "navy", "purple",
                 "teal", "silver", "grey", "red", "lime", "yellow", "blue", "fuchsia",
                 "aqua", "white"]
    for j in range(-1, 16):
        curses.init_pair(color_index, j, color_int_background)
        color_key = "{}_on_{}".format(color_str[j + 1], color_str_background)
        color_dict[color_key] = color_index
        color_index += 1
    return color_dict


def color_pair_integer(app, color_int=None):
    if not color_int and not app.color_default:
        return curses.color_pair(0)
    elif not color_int:
        return curses.color_pair(app.color_default)
    elif isinstance(color_int, str):
        return curses.color_pair(app.color_names[color_int])
    else:
        return curses.color_pair(color_int)



def format_text(arguments):
    attributes = []
    for arg in list(arguments.keys()):
        if arg.startswith("A_"):
            try:
                attributes.append(getattr(curses, arg))
            except AttributeError:
                pass
    if len(attributes) < 18:
        attributes = attributes + ([0] * (18 - len(attributes)))
    return attributes
