#! /usr/bin/env python3
import curses.panel
import curses
from dashport.colors import color_pair_integer as cpi

def title_bar(app, **kwargs):
    align = kwargs.get("align", "top")
    text = kwargs.get("text", "")
    color = kwargs.get("color", app.color_default)
    if align == "top":
        app.insstr(text.ljust(app.cols), x=0, y=0, color=color)
        app.title_offset = 1
        app.screen.setscrreg(1, app.rows - 1)
        app.top_title_row = 0
    elif align == "bottom":
        app.insstr(text.ljust(app.cols - 1),
                   x=0, y=app.rows - app.title_offset - 1, color=color)
        app.insstr(" ", x=app.cols - 1, y=app.rows - app.title_offset - 1,
                   color=color)
        app.bottom_title_row = app.rows - app.title_offset - 2
        app.title_bottom_offset = 1
        app.screen.setscrreg(0, app.rows - 2)

def button(app, **kwargs):
    button_name = kwargs.get("button_name")
    pos_x = kwargs.get("x")
    pos_y = kwargs.get("y")
    height = kwargs.get("height")
    width = kwargs.get("width")
    text = kwargs.get("text", None)
    color = kwargs.get("color", None)
    if kwargs.get("selected"):
        reverse = True
    else:
        reverse = False
    app.buttons[button_name] = app.panel(
        height=height, width=width, y=pos_y, x=pos_x,
        border=False)
    if color:
        for j in range(0, height):
            for i in range(0, width):
                if reverse:
                    app.buttons[button_name][0].insstr(j, i, " ", cpi(app, color) | curses.A_REVERSE)
                else:
                    app.buttons[button_name][0].insstr(j, i, " ", cpi(app, color))
    if text:
        if kwargs.get("h_align", "center") == "center":
            text = text.center(width - 2, " ")
        elif kwargs.get("h_align", "center") == "right":
            text = text.rjust(width - 2)
        elif kwargs.get("h_align", "center") == "left":
            text = text.ljust(width - 2)
        if kwargs.get("v_align", "center") == "center":
            row = int(height / 2)
        elif kwargs.get("v_align", "center") == "top":
            row = 0
        elif kwargs.get("v_align", "center") == "bottom":
            row = height - 1
        if reverse:
            app.buttons[button_name][0].insstr(row, 0, text, cpi(app, color) | curses.A_REVERSE)
        else:
            app.buttons[button_name][0].insstr(row, 0, text, cpi(app, color))
    curses.panel.update_panels()
    app.screen.refresh()