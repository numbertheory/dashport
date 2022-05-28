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
