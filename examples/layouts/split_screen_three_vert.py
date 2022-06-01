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
    app.split_screen_three_vert(border=True, long_side="right",
                                long_side_width=20)
    app.print("panel 0", x=1, y=1, panel="layout.0")
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2,
              panel="layout.0")
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3,
              panel="layout.0")
    app.print("panel 1", x=1, y=1, panel="layout.1")
    app.print(f"Rows: {app.panel_dimensions[1][0]}", x=5, y=2,
              panel="layout.1")
    app.print(f"Columns: {app.panel_dimensions[1][1]}", x=5, y=3,
              panel="layout.1")
    app.print("panel 2", x=1, y=1, panel="layout.2")
    app.print(f"Rows: {app.panel_dimensions[2][0]}", x=5, y=2,
              panel="layout.2")
    app.print(f"Columns: {app.panel_dimensions[2][1]}", x=5, y=3,
              panel="layout.2")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
