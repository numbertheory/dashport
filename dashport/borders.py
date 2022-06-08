#! /usr/bin/env python3
import curses
from dashport.characters import BoxDrawing


def custom_border(panel, characters):
    rows, cols = panel.getmaxyx()
    ul_corner = characters[0]  # upper left
    ur_corner = characters[1]  # upper right
    ll_corner = characters[2]  # lower left
    lr_corner = characters[3]  # lower right
    left_vert = characters[4]  # left vertical
    rght_vert = characters[5]  # right vertical
    top_horiz = characters[6]  # top horizontal
    btm_horiz = characters[7]  # bottom horizontal
    panel.addstr(0, 0, ul_corner)
    panel.addstr(0, cols - 1, ur_corner)
    panel.addstr(rows - 1, 0, ll_corner)
    panel.insstr(rows - 1, cols - 1, lr_corner)
    for i in range(1, rows - 1):
        panel.addstr(i, 0, left_vert)
        panel.addstr(i, cols - 1, rght_vert)
    for i in range(1, cols - 1):
        panel.addstr(0, i, top_horiz)
        panel.addstr(rows - 1, i, btm_horiz)
    curses.panel.update_panels()


def style(panel, border_style=None, **kwargs):
    boxes = BoxDrawing
    rows, cols = panel.getmaxyx()
    if border_style == 0:
        panel.border(curses.ACS_VLINE,
                     curses.ACS_VLINE,
                     curses.ACS_HLINE,
                     curses.ACS_HLINE,
                     curses.ACS_ULCORNER,
                     curses.ACS_URCORNER,
                     curses.ACS_LLCORNER,
                     curses.ACS_LRCORNER)
    elif border_style == 1:
        panel.border('|', '|', '-', '-', '+', '+', '+', '+')
    elif border_style == 2:
        panel.border('\\', '/', '=', '=', ' ', ' ', ' ', ' ')
    elif border_style == 3:
        characters = [
            chr(boxes.html("double_down_and_right")),
            chr(boxes.html("double_down_and_left")),
            chr(boxes.html("double_up_and_right")),
            chr(boxes.html("double_up_and_left")),
            chr(boxes.html("double_vertical")),
            chr(boxes.html("double_vertical")),
            chr(boxes.html("double_horizontal")),
            chr(boxes.html("double_horizontal"))
        ]
        custom_border(panel, characters)
