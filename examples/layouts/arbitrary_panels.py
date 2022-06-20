#!/usr/bin/env python3

from dashport.dash import Dashport
from dashport.run import wrap


def quit(app):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default="red_on_blue")
    app.add_control("q", quit, case_sensitive=False)
    app.layout("single_panel")
    app.print("This is the first panel in the layout.", x=5, y=2, panel="layout.0")
    app.panels["some_panel"] = app.panel(height=3, width=25, y=20, x=20, border=True, border_style=3)
    app.print("this is another panel", x=1, y=1, panel="some_panel.0")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)