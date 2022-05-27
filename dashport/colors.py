#!/usr/bin/env python3

import curses


def color_defs():
    color_index = 1
    for k in range(-1, 34):
        for j in range(0, 8):
            curses.init_pair(color_index, j, k)
            color_index += 1
