#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app)


def quit(app):
    exit(0)


def scroll_down(app):
    app.screen.scroll(1)


def dashport(stdscr):
    app = Dashport(stdscr, scroll=True)
    app.add_control("q", quit)
    app.add_control("KEY_DOWN", scroll_down)
    rows, cols = app.screen.getmaxyx()
    app.split_screen_columns(borders=True)
    app.title_bar(text=f"Title {app.cursor_x},{app.cursor_y}",
                  align="top", color=256)
    for i in range(0, 41):
        app.print(content=f"Line: {i} {app.cursor_y}", x=1, y=i+1, panel=1)

    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
