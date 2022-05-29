#! /usr/bin/env python3
import curses


def split_screen_columns(app, **kwargs):
    split_cols = int(app.cols / 2)
    win1, panel1 = app.panel(height=app.rows, length=split_cols, y=0, x=0,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    win2, panel2 = app.panel(height=app.rows, length=split_cols,
                             y=0,
                             x=split_cols,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def split_screen_rows(app, **kwargs):
    split_rows = int(app.rows / 2)
    win1, panel1 = app.panel(height=split_rows, length=app.cols, y=0, x=0,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    win2, panel2 = app.panel(height=split_rows, length=app.cols,
                             y=split_rows,
                             x=0,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def quadrants(app, **kwargs):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    win1, panel1 = app.panel(height=split_rows, length=split_cols,
                             y=0, x=0,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    win2, panel2 = app.panel(height=split_rows, length=split_cols,
                             y=0, x=split_cols,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    win3, panel3 = app.panel(height=split_rows, length=split_cols,
                             y=split_rows, x=0,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    win4, panel4 = app.panel(height=split_rows, length=split_cols,
                             y=split_rows, x=split_cols,
                             scroll=kwargs.get("scroll", True),
                             border=kwargs.get("border", False))
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx(), win4.getmaxyx()]
    return [win1, win2, win3, win4, panel1, panel2, panel3, panel4]


def three_panels_vert(app, **kwargs):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    long_side = kwargs.get("long_side", "right")
    border = kwargs.get("border", False)
    long_side_width = kwargs.get("long_side_width", None)
    if not long_side_width:
        long_side_width = split_cols
    if long_side == "right":
        win1, panel1 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", True),
                                 y=0, x=0, border=border)
        win2, panel2 = app.panel(
            height=app.rows - app.title_offset - app.title_bottom_offset,
            length=long_side_width,
            y=0, x=app.cols - long_side_width,
            scroll=kwargs.get("scroll", True),
            border=border)
        win3, panel3 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", True),
                                 y=split_rows, x=0, border=border)
    elif long_side == "left":
        win1, panel1 = app.panel(
            height=app.rows - app.title_offset - app.title_bottom_offset,
            length=long_side_width,
            scroll=kwargs.get("scroll", True),
            y=0, x=0, border=border)
        win2, panel2 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", True),
                                 y=0, x=long_side_width, border=border)
        win3, panel3 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 y=split_rows, x=long_side_width,
                                 scroll=kwargs.get("scroll", True),
                                 border=border)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]


def three_panels_horizontal(app, **kwargs):
    split_rows = int(app.rows / 2)
    split_cols = int(app.cols / 2)
    long_side = kwargs.get("long_side", "top")
    border = kwargs.get("border", False)
    long_side_height = kwargs.get("long_side_height", None)
    if not long_side_height:
        long_side_height = split_rows
    if long_side == "top":
        win1, panel1 = app.panel(height=long_side_height,
                                 length=app.cols,
                                 scroll=kwargs.get("scroll", True),
                                 y=0, x=0, border=border)
        win2, panel2 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", True),
                                 y=long_side_height, x=0, border=border)
        win3, panel3 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", True),
                                 y=long_side_height, x=split_cols,
                                 border=border)
    elif long_side == "bottom":
        win1, panel1 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", True),
                                 y=0, x=0, border=border)
        win2, panel2 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", True),
                                 y=0, x=split_cols, border=border)
        win3, panel3 = app.panel(height=long_side_height, length=app.cols,
                                 y=app.rows - long_side_height, x=0,
                                 scroll=kwargs.get("scroll", True),
                                 border=border)
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]
