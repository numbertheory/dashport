#!/usr/bin/env python3
from dashport.dash import Dashport
from dashport.run import wrap
from dashport.characters import BoxDrawing, BlockElements


class Select:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.current_view = "block_elements"
        self.cv_index = 0
        self.last_cell = {"line_drawing": [12, 7],
                          "block_elements": [3, 1]}
        self.last_cell_values = {"line_drawing": [11, 12, 9],
                                 "block_elements": [2, 3, 9]}
        first_key = sorted(
            BoxDrawing.data().items(),
            key=self.by_value)[0][0]
        self.current_selection = first_key

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
    last_cell_values = selector.last_cell_values[selector.current_view]
    if selector.row < last_cell_values[2] and current_pos != last_cell:
        selector.row += 1


def move_left(app):
    if 0 < selector.column:
        selector.column -= 1


def move_right(app):
    projected_pos = [selector.column + 1, selector.row]
    last_cell = selector.last_cell[selector.current_view]
    last_cell_values = selector.last_cell_values[selector.current_view]
    check_col = projected_pos[0] <= last_cell[0]
    if projected_pos[0] > last_cell_values[0]:
        check_row = projected_pos[1] <= last_cell[1]
    else:
        check_row = True
    if selector.column < last_cell_values[1] and check_col and check_row:
        selector.column += 1


def change_view(app):
    app.screen.clear()
    app.widget("title_bar", text="Q = quit, B = Next page",
               align="bottom", color=121)
    if selector.current_view == "line_drawing":
        selector.current_view = "block_elements"
        selector.cv_index = 0
        selector.column = 0
        selector.row = 0
    else:
        selector.current_view = "line_drawing"
        selector.cv_index = 1
        selector.column = 0
        selector.row = 0


def table_drawing(app, selection, table):
    index_of_everything = [0, 0]
    column = 3
    row = 3
    table_elements = table["elements"].data()

    for key, value in sorted(table_elements.items(), key=by_value):
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
    extra_space = " " * (app.cols - len(python_content))
    app.print(panel="layout.0",
              content=python_content + extra_space, x=2, y=24)
    app.print(panel="layout.0",
              content="HTML: &#{};".format(
                table["elements"].html(selector.current_selection)),
              x=2, y=25)
    app.print(panel="layout.0",
              content="Unicode: U+{}".format(
                table["elements"].unicode(selector.current_selection)),
              x=2, y=26)


def dashport(stdscr):
    app = Dashport(stdscr)
    height = app.rows - 2
    app.widget("title_bar", text="Q = quit, B = Next page",
               align="bottom", color=121)
    app.layout("single_panel", scroll=True, height=height)
    app.add_control("q", quit)
    app.add_control("KEY_UP", move_up)
    app.add_control("KEY_DOWN", move_down)
    app.add_control("KEY_LEFT", move_left)
    app.add_control("KEY_RIGHT", move_right)
    app.add_control("B", change_view, case_sensitive=False)
    table = [{"elements": BlockElements, "name": "block_elements",
              "display_name": "Block Elements"},
             {"elements": BoxDrawing, "name": "line_drawing",
              "display_name": "Box Drawing"}]
    while True:
        table_drawing(app, [selector.column, selector.row],
                      table[selector.cv_index])
        app.print(panel="layout.0",
                  content="{} Group".format(
                    table[selector.cv_index]["display_name"]),
                  x=1, y=1)
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)
