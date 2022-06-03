#!/usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap
from dashport.characters import box_drawings


class Select:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.current_view = "line_drawing"
        self.last_cell = {"line_drawing": [12, 7]}


selector = Select()


def quit(app):
    exit(0)


def by_value(item):
    return item[1]


def move_up(app):
    if 0 < selector.row:
        selector.row -= 1


def move_down(app):
    current_pos = [selector.column, selector.row]
    last_cell = selector.last_cell[selector.current_view]
    if selector.row < 9 and current_pos != last_cell:
        selector.row += 1


def move_left(app):
    if 0 < selector.column:
        selector.column -= 1


def move_right(app):
    projected_pos = [selector.column + 1, selector.row]
    last_cell = selector.last_cell[selector.current_view]
    check_col = projected_pos[0] <= last_cell[0]
    check_row = projected_pos[1] <= last_cell[1]
    if selector.column < 12 and check_col and check_row:
        selector.column += 1


def line_drawing(app, selection):
    index_of_everything = [0, 0]
    column = 3
    row = 3
    box_drawing = box_drawings()

    for key, value in sorted(box_drawing.items(), key=by_value):
        if index_of_everything == selection:
            app.print(panel="layout.0",
                      x=column - 1,
                      y=row,
                      color=65,
                      content=" {} ".format(chr(value)))
        else:
            app.print(panel="layout.0",
                      x=column - 1,
                      y=row,
                      content=" {} ".format(chr(value)))
        app.screen.refresh()
        if row >= 20:
            row = 3
            column += 4
            index_of_everything[0] += 1
            index_of_everything[1] = 0
        else:
            row += 2
            index_of_everything[1] += 1


def dashport(stdscr):
    app = Dashport(stdscr)
    height = app.rows - 4
    app.single_panel(scroll=True, height=height, border=True)
    app.add_control("q", quit)
    app.add_control("KEY_UP", move_up)
    app.add_control("KEY_DOWN", move_down)
    app.add_control("KEY_LEFT", move_left)
    app.add_control("KEY_RIGHT", move_right)
    while True:
        line_drawing(app, [selector.column, selector.row])
        app.print(panel="layout.0",
                  content="Box Drawing Group {}".format(
                    [selector.column, selector.row]), x=1, y=1)
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
