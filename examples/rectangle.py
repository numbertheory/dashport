#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def quit(stdscr):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=17)
    app.add_control("q", quit, case_sensitive=False)
    # This text won't show because the background will overwrite it.
    app.print("This text won't show.", x=5, y=5)
    # Color 109 is a blue background
    app.background(color=109)
    # This text will show because it comes after the background.
    app.print("printing on top of text")
    app.rectangle(10, 10, 12, 12, color=98)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
