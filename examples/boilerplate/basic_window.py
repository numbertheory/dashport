#! /usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap


def quit(app):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=8)
    app.add_control("q", quit, case_sensitive=False)
    app.single_panel(border=True)
    app.print("This text is bold.", A_BOLD=True, panel="layout.0", x=1, y=1)
    app.print("This text is reversed.", A_REVERSE=True, panel="layout.0", x=1, y=2)
    app.print("This text is normal.", panel="layout.0", x=1, y=3)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
