#! /usr/bin/env python3

def title_bar(app, **kwargs):
    align = kwargs.get("align", "top")
    text = kwargs.get("text", "")
    color = kwargs.get("color", app.color_default)
    if align == "top":
        app.print(content=text.ljust(app.cols), x=0, y=0, color=color, end="")
        app.title_offset = 1
        app.screen.setscrreg(1, app.rows - 1)
    elif align == "bottom":
        app.title_offset = 0
        app.print(content=text.ljust(app.cols - 1),
                  x=0, y=app.rows - 1, color=color)
        app.insstr(" ", x=app.cols - 1, y=app.rows - 1, color=color)
        app.title_bottom_offset = 1
        app.screen.setscrreg(app.title_offset, app.rows - 2)
