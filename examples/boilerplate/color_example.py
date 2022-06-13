#!/usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap

def dashport(stdscr):
    app = Dashport(stdscr, color_default="green_on_white")
    app.print("hello world", color="red_on_white")
    app.print("plain text, colored with color_default")
    app.print("black text on blue background", color="black_on_blue")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
