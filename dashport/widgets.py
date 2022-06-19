#! /usr/bin/env python3

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
    border = kwargs.get("border", True)
    if app.selected_button == button_name:
        border_style = 3
    else:
        border_style = 0
    app.buttons[button_name] = app.panel(
        height=height, length=width, y=pos_y, x=pos_x,
        border=border,
        border_style=border_style)
    app.screen.refresh()