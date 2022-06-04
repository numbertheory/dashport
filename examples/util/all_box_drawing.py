#!/usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap
from dashport.characters import BoxDrawing


class Select:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.current_view = "line_drawing"
        self.last_cell = {"line_drawing": [12, 7]}
        first_key = sorted(
            BoxDrawing.data().items(),
            key=self.by_value)[0][0]
        self.current_selection = "BoxDrawing." \
                                 "char('{}')".format(first_key)

    def by_value(self, item):
        return item[1]


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
    if projected_pos[0] > 11:
        check_row = projected_pos[1] <= last_cell[1]
    else:
        check_row = True
    if selector.column < 12 and check_col and check_row:
        selector.column += 1


def line_drawing(app, selection):
    index_of_everything = [0, 0]
    column = 3
    row = 3
    box_drawing = BoxDrawing.data()

    for key, value in sorted(box_drawing.items(), key=by_value):
        if index_of_everything == selection:
            selector.current_selection = key
            app.print(panel="layout.0",
                      x=column - 1,
                      y=row,
                      color=121,
                      content=" {} ".format(chr(value[0])))
        else:
            app.print(panel="layout.0",
                      x=column - 1,
                      y=row,
                      content=" {} ".format(chr(value[0])))

        if row >= 20:
            row = 3
            column += 4
            index_of_everything[0] += 1
            index_of_everything[1] = 0
        else:
            row += 2
            index_of_everything[1] += 1
    python_content = "Name: {}".format(selector.current_selection)
    extra_space = " " * (app.cols - (56 + len(python_content)))
    app.print(panel="layout.0",
              content=python_content + extra_space, x=2, y=24)
    app.print(panel="layout.0",
              content="HTML: &#{};".format(
                BoxDrawing.html(selector.current_selection)),
              x=2, y=25)
    app.print(panel="layout.0",
              content="Unicode: U+{}".format(
                BoxDrawing.unicode(selector.current_selection)),
              x=2, y=26)


def dashport(stdscr):
    app = Dashport(stdscr)
    height = app.rows - 1
    app.title_bar(text="Q = quit, Tab = Next page", align="top", color=121)
    app.single_panel(scroll=True, height=height)
    app.add_control("q", quit)
    app.add_control("KEY_UP", move_up)
    app.add_control("KEY_DOWN", move_down)
    app.add_control("KEY_LEFT", move_left)
    app.add_control("KEY_RIGHT", move_right)
    while True:
        line_drawing(app, [selector.column, selector.row])
        app.print(panel="layout.0",
                  content="Box Drawing Group", x=1, y=1)
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
