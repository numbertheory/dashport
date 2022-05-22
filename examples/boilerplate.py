#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr)

    # This loop refreshes the screen. Don't put any other commands
    # in this loop, instead add to the `app` object above, and let
    # this loop run.
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
