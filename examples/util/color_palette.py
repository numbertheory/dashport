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
    for j in range(1, 33):
        app.print(f"Color {str(j)}", x=0, color=j)
    app.cursor_y = 0
    for j in range(33, 65):
        app.print(f"Color {str(j)}", x=10, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(65, 97):
        app.print(f"Color {str(j)}", x=20, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(97, 129):
        app.print(f"Color {str(j)}", x=30, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(129, 161):
        app.print(f"Color {str(j)}", x=40, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(161, 193):
        app.print(f"Color {str(j)}", x=50, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(193, 225):
        app.print(f"Color {str(j)}", x=60, color=j)
        app.cursor_y += 1
    app.cursor_y = 0
    for j in range(225, 257):
        app.print(f"Color {str(j)}", x=70, color=j)
        app.cursor_y += 1
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
