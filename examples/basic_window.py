#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    keymap = {"q": "quit", "Q": "quit"}
    app = Dashport(stdscr, keys=keymap)
    app.print("Press 'q' to exit.")
    app.print("")
    app.print("Printing multiple lines is as easy as Python's standard print.")
    app.print("And you can locate strings wherever you want.", x=15, y=10)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
