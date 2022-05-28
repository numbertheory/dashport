#! /usr/bin/env python3
import curses


def split_screen_columns(app, borders=False):
    split_cols = int(app.cols / 2)
    win1, panel1 = app.panel(app.rows, split_cols, 0, 0, borders)
    win2, panel2 = app.panel(app.rows, split_cols, 0, split_cols, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def split_screen_rows(app, borders=False):
    split_rows = int(app.rows / 2)
    win1, panel1 = app.panel(split_rows, app.cols, 0, 0, borders)
    win2, panel2 = app.panel(split_rows, app.cols, split_rows, 0, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def quadrants(app, borders=False):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    win1, panel1 = app.panel(split_rows, split_cols,
                             0, 0, borders)
    win2, panel2 = app.panel(split_rows, split_cols,
                             0, split_cols, borders)
    win3, panel3 = app.panel(split_rows, split_cols,
                             split_rows, 0, borders)
    win4, panel4 = app.panel(split_rows, split_cols,
                             split_rows, split_cols, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx(), win4.getmaxyx()]
    return [win1, win2, win3, win4, panel1, panel2, panel3, panel4]


def three_panels_vert(app, borders=False, long_side="right",
                      long_side_width=None):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    if not long_side_width:
        long_side_width = split_cols
    if long_side == "right":
        win1, panel1 = app.panel(split_rows, app.cols - long_side_width,
                                 0, 0, borders)
        win2, panel2 = app.panel(app.rows - app.title_offset, long_side_width,
                                 0, app.cols - long_side_width, borders)
        win3, panel3 = app.panel(split_rows, app.cols - long_side_width,
                                 split_rows, 0, borders)
    elif long_side == "left":
        win1, panel1 = app.panel(app.rows, long_side_width,
                                 0, 0, borders)
        win2, panel2 = app.panel(split_rows, app.cols - long_side_width,
                                 0, long_side_width, borders)
        win3, panel3 = app.panel(split_rows, app.cols - long_side_width,
                                 split_rows, long_side_width, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]


def three_panels_horizontal(app, borders=False, long_side="top",
                            long_side_height=None):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    if not long_side_height:
        long_side_height = split_rows
    if long_side == "top":
        win1, panel1 = app.panel(long_side_height, app.cols,
                                 0, 0, borders)
        win2, panel2 = app.panel(app.rows - long_side_height, split_cols,
                                 long_side_height, 0, borders)
        win3, panel3 = app.panel(app.rows - long_side_height, split_cols,
                                 long_side_height, split_cols, borders)
    elif long_side == "bottom":
        win1, panel1 = app.panel(app.rows - long_side_height, split_cols,
                                 0, 0, borders)
        win2, panel2 = app.panel(app.rows - long_side_height, split_cols,
                                 0, split_cols, borders)
        win3, panel3 = app.panel(long_side_height, app.cols,
                                 app.rows - long_side_height, 0, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]
