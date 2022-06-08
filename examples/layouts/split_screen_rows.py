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
    app.layout("split_screen_rows", border=True)
    app.print("layout.0", x=1, y=1, panel="layout.0", color=176)
    app.print("layout.1", x=1, y=1, panel="layout.1", color=176)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
