#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app.screen)


def quit(app):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=17)
    app.add_control("q", quit, case_sensitive=False)
    app.split_screen_columns(border=True)
    app.print("hello", panel=1)
    app.print("world", panel=1)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)