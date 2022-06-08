#!/usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap
from dashport.borders import custom_border
from dashport.characters import BoxDrawing as boxes


def quit(app):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=176)
    app.add_control("q", quit, case_sensitive=False)
    app.layout("single_panel")
    border_characters = [
            chr(boxes.html("double_down_and_right")),  # upper left
            chr(boxes.html("double_down_and_left")),   # upper right
            chr(boxes.html("double_up_and_right")),    # lower left
            chr(boxes.html("double_up_and_left")),     # lower right
            chr(boxes.html("double_vertical")),        # left vertical
            chr(boxes.html("double_vertical")),        # right vertical
            chr(boxes.html("double_horizontal")),      # top horizontal
            chr(boxes.html("double_horizontal"))       # bottom horizontal
    ]
    custom_border(app.panels["layout"][0], border_characters)
    app.print("panel 0", x=5, y=2, panel="layout.0")
    app.print(f"Rows: {app.panel_dimensions[0][0]}",
              x=5, y=3, panel="layout.0")
    app.print(f"Columns: {app.panel_dimensions[0][1]}",
              x=5, y=4, panel="layout.0")

    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
