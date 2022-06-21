#!/usr/bin/env python3

from dashport.dash import Dashport
from dashport.run import wrap


def quit(app):
    exit(0)

def quick_output_panel(app):
    app.print("quick was clicked", x=1, y=4, panel="output.0")

def brown_output_panel(app):
    app.print("brown was clicked", x=1, y=4, panel="output.0")

def fox_output_panel(app):
    app.print("fox was clicked  ", x=1, y=4, panel="output.0")

def clear_output_panel(app):
    app.print("                 ", x=1, y=4, panel="output.0")

def cycle_buttons(app):
    clear_output_panel(app)
    button_names = ["quick", "brown", "fox"]
    next_index = button_names.index(app.selected_button) + 1
    if next_index == 3:
        next_index = 0
    app.selected_button = button_names[next_index]
    selection = [False, False, False]
    selection[next_index] = True
    app.widget("button", button_name="quick", 
               color="default_on_blue",
               text="quick",
               action=quick_output_panel, action_keys=["\n", "KEY_ENTER"],
               x=1, y=1, height=5, width=13, selected=selection[0])
    app.widget("button", button_name="brown",
               color="default_on_blue", text="brown", 
               action=brown_output_panel, action_keys=["\n", "KEY_ENTER"],
               x=1, y=7, height=5, width=13, selected=selection[1])
    app.widget("button", button_name="fox",
               color="default_on_blue", text="fox", 
               action=fox_output_panel, action_keys=["\n", "KEY_ENTER"],
               x=1, y=13, height=5, width=13, selected=selection[2])


def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit, case_sensitive=False)
    app.add_control("\t", cycle_buttons, case_sensitive=False)
    app.layout("single_panel", border=True)
    app.panels["output"] = app.panel(height=10, width=30, y=5, x=25,
                             border=True)
    app.print("Button activation demo", x=1, y=1, panel="output.0")
    app.selected_button = "fox"
    cycle_buttons(app)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
