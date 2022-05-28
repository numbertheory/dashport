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
    app.window.scrollok(True)
    app.window.idlok(True)
    rows, cols = app.screen.getmaxyx()
    for i in range(0, app.rows + 1):
        app.print(f"Line: {i}")

    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
