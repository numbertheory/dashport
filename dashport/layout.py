#! /usr/bin/env python3
import curses


def split_screen_columns(app, borders=False):
    split_cols = int(app.cols / 2)
    win1, panel1 = app.panel(app.rows, split_cols, 0, 0, borders)
    win2, panel2 = app.panel(app.rows, split_cols, 0, split_cols, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    return [win1, win2, panel1, panel2]


def split_screen_rows(app, borders=False):
    split_rows = int(app.rows / 2)
    win1, panel1 = app.panel(split_rows, app.cols, 0, 0, borders)
    win2, panel2 = app.panel(split_rows, app.cols, split_rows, 0, borders)
    curses.panel.update_panels()
    app.screen.refresh()
    return [win1, win2, panel1, panel2]
