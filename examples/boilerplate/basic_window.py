#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=8)
    app.print("This text is bold", A_BOLD=True)
    app.print("This text is reversed", A_REVERSE=True)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
