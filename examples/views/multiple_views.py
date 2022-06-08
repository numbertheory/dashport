#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app.screen)


def quit(app):
    exit(0)


def four_way_split(app):
    app.layout("quadrants", border=True, height=app.rows - 2)
    app.print("panel 0", panel="layout.0")
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2,
              panel="layout.0")
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3,
              panel="layout.0")
    app.print("panel 1", panel="layout.1")
    app.print(f"Rows: {app.panel_dimensions[1][0]}", x=5, y=2,
              panel="layout.1")
    app.print(f"Columns: {app.panel_dimensions[1][1]}", x=5, y=3,
              panel="layout.1")
    app.print("panel 2", panel="layout.2")
    app.print(f"Rows: {app.panel_dimensions[2][0]}", x=5, y=2,
              panel="layout.2")
    app.print(f"Columns: {app.panel_dimensions[2][1]}", x=5, y=3,
              panel="layout.2")
    app.print("panel 3", panel="layout.3")
    app.print(f"Rows: {app.panel_dimensions[3][0]}", x=5, y=2,
              panel="layout.3")
    app.print(f"Columns: {app.panel_dimensions[3][1]}", x=5, y=3,
              panel="layout.3")


def three_way_split(app):
    app.layout("three_panels_vert", border=True, long_side="right",
               long_side_width=100)
    app.print("panel 0", panel="layout.0")
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2,
              panel="layout.0")
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3,
              panel="layout.0")
    app.print("panel 1", panel="layout.1")
    app.print(f"Rows: {app.panel_dimensions[1][0]}", x=5, y=2,
              panel="layout.1")
    app.print(f"Columns: {app.panel_dimensions[1][1]}", x=5, y=3,
              panel="layout.1")
    app.print("panel 2", panel="layout.2")
    app.print(f"Rows: {app.panel_dimensions[2][0]}", x=5, y=2,
              panel="layout.2")
    app.print(f"Columns: {app.panel_dimensions[2][1]}", x=5, y=3,
              panel="layout.2")


def dashport(stdscr):
    app = Dashport(stdscr, color_default=176,  scroll=True)
    app.add_control("q", quit, case_sensitive=False)
    app.wisdget("title_bar",
                text="Press 4 to split 4 ways, 3 to split 3 ways, "
                "Q to quit.",
                align="top", color=256)
    three_way_split(app)
    app.add_control("4", four_way_split)
    app.add_control("3", three_way_split)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
