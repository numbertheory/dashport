#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap

"""
This demo needs at least 80 columns and 32 lines to work.
"""


def quit(*args):
    exit(0)


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=9)
    app.add_control("q", quit, case_sensitive=False)
    color_names = list(app.color_names.keys())
    for j in range(1, 34):
        app.print(f"{color_names[j]}", x=0, color=color_names[j])
    app.cursor_y = 0
    for j in range(34, 67):
        app.print(f"{color_names[j]}", x=20, color=color_names[j])
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(67, 99):
       app.print(f"{color_names[j]}", x=40, color=color_names[j])
       app.cursor_y += 1
    app.cursor_y = 0
    for j in range(99, 131):
        app.print(f"{color_names[j]}", x=60, color=color_names[j])
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(131, 163):
        app.print(f"{color_names[j]}", x=80, color=color_names[j])
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(161, 193):
        app.print(f"{color_names[j]}", x=100, color=color_names[j])
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(193, 225):
        app.print(f"{color_names[j]}", x=120, color=color_names[j])
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(225, 255):
        app.print(f"{color_names[j]}", x=140, color=color_names[j])
        app.cursor_y += 1
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
