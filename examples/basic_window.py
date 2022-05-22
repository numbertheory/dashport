#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def quit(*args):
    exit(0)


def add_text(app):
    app.print("hello", x=16, y=13)


def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit)
    app.add_control("k", add_text)
    app.print("Press 'q' to exit.")
    app.print("Press 'k' to print a new string")
    app.print("Printing multiple lines is as easy as Python's standard print.")
    app.print("And you can locate strings wherever you want.", x=15, y=10)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
