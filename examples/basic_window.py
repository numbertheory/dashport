#! /usr/bin/env python3
from curses import wrapper
from dashport.dash import Dashport


def dashport(stdscr):
    keymap = {"q": "quit"}
    app = Dashport(stdscr, keys=keymap)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrapper(dashport)
