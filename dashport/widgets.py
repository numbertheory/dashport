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
