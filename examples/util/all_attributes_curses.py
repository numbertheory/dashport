#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap
import curses


def info(stdscr):
    return Info(stdscr)


def quit(*args):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, scroll=True)
    app.add_control("q", quit)
    app.print("Press 'q' to exit.")
    app.print("")
    curses_constants = [{"name": x, "integer": getattr(curses, x)}
                        for x in dir(curses) if x.startswith("A_")]
    for i in range(0, 9):
        app.print("{}".format(curses_constants[i]["name"]))
        app.addstr("{} ".format(curses_constants[i]["integer"]),
                   x=15, y=app.cursor_y - 1)
    count_line = 2
    for i in range(9, 18):
        app.print("{}".format(curses_constants[i]["name"]), x=30, y=count_line)
        app.addstr("{} ".format(curses_constants[i]["integer"]),
                   x=44, y=count_line)
        count_line += 1
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
