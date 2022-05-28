#! /usr/bin/env python3

def title_bar(app, text, align="top"):
    if align == "top":
        app.print(content=text.ljust(app.cols), x=0, y=0)
        app.title_offset = 1
    elif align == "bottom":
        app.print(content=text.ljust(app.cols - 1), x=0, y=app.rows - 1)
        app.title_bottom_offset = 1
