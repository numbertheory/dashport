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
    app.layout("quadrants",
               border=[True, False, True, True],
               border_styles=[0, 1, 1, 3])
    # app.panels["layout"][3].border('M', 'M', '=', '=', ' ', ' ', ' ', ' ')
    app.print("panel: layout.0", x=1, y=1, panel="layout.0",
              A_BOLD=True, A_ITALIC=True)
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2,
              panel="layout.0", A_REVERSE=True)
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3,
              panel="layout.0", A_REVERSE=True)
    app.print("panel: layout.1", x=1, y=1, panel="layout.1",
              A_BOLD=True, A_ITALIC=True)
    app.print(f"Rows: {app.panel_dimensions[1][0]}", x=5, y=2,
              panel="layout.1", A_REVERSE=True)
    app.print(f"Columns: {app.panel_dimensions[1][1]}", x=5, y=3,
              panel="layout.1", A_REVERSE=True)
    app.print("panel: layout.2", x=1, y=1, panel="layout.2",
              A_BOLD=True, A_ITALIC=True)
    app.print(f"Rows: {app.panel_dimensions[2][0]}", x=5, y=2,
              panel="layout.2", A_REVERSE=True)
    app.print(f"Columns: {app.panel_dimensions[2][1]}", x=5, y=3,
              panel="layout.2", A_UNDERLINE=True)
    app.print("panel: layout.3", x=1, y=1, panel="layout.3",
              A_BOLD=True, A_ITALIC=True)
    app.print(f"Rows: {app.panel_dimensions[3][0]}", x=5, y=2,
              panel="layout.3", A_REVERSE=True)
    app.print(f"Columns: {app.panel_dimensions[3][1]}", x=5, y=3,
              panel="layout.3", A_UNDERLINE=True)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
