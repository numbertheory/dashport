#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app)


def quit(app):
    exit(0)

def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit)

    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
