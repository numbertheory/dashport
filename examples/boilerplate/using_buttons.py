#!/usr/bin/env python3

from dashport.dash import Dashport
from dashport.run import wrap

def quit(app):
    exit(0)

def cycle_buttons(app):
    app.selected_button = "brown"
    app.widget("button", button_name="quick", x=1, y=1, height=4, width=8)
    app.widget("button", button_name="brown", x=1, y=5, height=4, width=8)
    app.widget("button", button_name="fox", x=1, y=9, height=4, width=8)

def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit, case_sensitive=False)
    app.add_control("\t", cycle_buttons, case_sensitive=False)
    app.layout("single_panel", border=True)
    while True:
        app.widget("button", button_name="quick", x=1, y=1, height=4, width=8)
        app.widget("button", button_name="brown", x=1, y=5, height=4, width=8)
        app.widget("button", button_name="fox", x=1, y=9, height=4, width=8)
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
