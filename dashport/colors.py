#!/usr/bin/env python3

import curses


def color_defs():
    color_index = 1
    for k in range(-1, 34):
        for j in range(0, 8):
            curses.init_pair(color_index, j, k)
            color_index += 1


def color_pair_integer(default, color_int=None):
    if not color_int:
        return curses.color_pair(default)
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
