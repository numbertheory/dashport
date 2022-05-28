#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app.screen)


def quit(app):
    exit(0)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=176)
    app.add_control("q", quit, case_sensitive=False)
    app.split_screen_quad(borders=True)
    app.print("panel 0", panel=0)
    app.print(f"{app.panel_dimensions[0]}", panel=0)
    app.print("panel 1", panel=1)
    app.print(f"{app.panel_dimensions[1]}", panel=1)
    app.print("panel 2", panel=2)
    app.print(f"{app.panel_dimensions[2]}", panel=2)
    app.print("panel 3", panel=3)
    app.print(f"{app.panel_dimensions[3]}", panel=3)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
