#! /usr/bin/env python3
import curses


def single_panel(app, **kwargs):
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0])
    height = kwargs.get("height", app.rows - app.title_offset)
    width = kwargs.get("width", app.cols)
    if isinstance(border, bool):
        border = [border]
    win1, panel1 = app.panel(height=height, length=width, y=0, x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[0],
                             border_style=border_styles[0])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0]]
    app.panel_dimensions = [win1.getmaxyx()]
    return [win1, panel1]


def split_screen_columns(app, **kwargs):
    if not kwargs.get("center_divide_x"):
        split_cols = int(app.cols / 2)
    else:
        split_cols = int(kwargs.get("center_divide_x"))
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0, 0])
    if isinstance(border, bool):
        border = [border] * 2
    win1, panel1 = app.panel(height=app.rows - app.title_offset,
                             length=split_cols, y=0, x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[0],
                             border_style=border_styles[0])
    win2, panel2 = app.panel(height=app.rows - app.title_offset,
                             length=split_cols,
                             y=0,
                             x=split_cols,
                             scroll=kwargs.get("scroll", False),
                             border=border[1],
                             border_style=border_styles[1])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def split_screen_rows(app, **kwargs):
    if not kwargs.get("center_divide_y"):
        split_rows = [int(app.rows / 2) - app.title_offset, int(app.rows / 2)]
    else:
        split_rows = [int(kwargs.get("center_divide_y")),
                      app.rows - int(kwargs.get("center_divide_y"))]
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0, 0])
    if isinstance(border, bool):
        border = [border] * 2
    win1, panel1 = app.panel(height=split_rows[0], length=app.cols, y=0, x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[0],
                             border_style=border_styles[0])
    win2, panel2 = app.panel(height=split_rows[1], length=app.cols,
                             y=split_rows[0],
                             x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[1],
                             border_style=border_styles[1])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx()]
    return [win1, win2, panel1, panel2]


def quadrants(app, **kwargs):
    split_rows = int(app.rows / 2) - app.title_offset
    split_cols = int(app.cols / 2)
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0, 0, 0, 0])
    if isinstance(border, bool):
        border = [border] * 4
    win1, panel1 = app.panel(height=split_rows, length=split_cols,
                             y=0, x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[0],
                             border_style=border_styles[0])
    win2, panel2 = app.panel(height=split_rows, length=split_cols,
                             y=0, x=split_cols,
                             scroll=kwargs.get("scroll", False),
                             border=border[1],
                             border_style=border_styles[1])
    win3, panel3 = app.panel(height=split_rows, length=split_cols,
                             y=split_rows, x=0,
                             scroll=kwargs.get("scroll", False),
                             border=border[2],
                             border_style=border_styles[2])
    win4, panel4 = app.panel(height=split_rows, length=split_cols,
                             y=split_rows, x=split_cols,
                             scroll=kwargs.get("scroll", False),
                             border=border[3],
                             border_style=border_styles[3])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx(), win4.getmaxyx()]
    return [win1, win2, win3, win4, panel1, panel2, panel3, panel4]


def three_panels_vert(app, **kwargs):
    split_rows = int(app.rows / 2) - app.title_offset
    split_cols = int(app.cols / 2)
    long_side = kwargs.get("long_side", "right")
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0, 0, 0])
    if isinstance(border, bool):
        border = [border] * 3
    long_side_width = kwargs.get("long_side_width", None)
    if not long_side_width:
        long_side_width = split_cols
    if long_side == "right":
        win1, panel1 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", False),
                                 y=0, x=0, border=border[0],
                                 border_style=border_styles[0])
        win2, panel2 = app.panel(
            height=app.rows - app.title_offset - app.title_bottom_offset,
            length=long_side_width,
            y=0, x=app.cols - long_side_width,
            scroll=kwargs.get("scroll", False),
            border=border[1],
            border_style=border_styles[1])
        win3, panel3 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", False),
                                 y=split_rows, x=0, border=border[2],
                                 border_style=border_styles[2])
    elif long_side == "left":
        win1, panel1 = app.panel(
            height=app.rows - app.title_offset - app.title_bottom_offset,
            length=long_side_width,
            scroll=kwargs.get("scroll", False),
            y=0, x=0, border=border[0],
            border_style=border_styles[0])
        win2, panel2 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 scroll=kwargs.get("scroll", False),
                                 y=0, x=long_side_width, border=border[1],
                                 border_style=border_styles[1])
        win3, panel3 = app.panel(height=split_rows,
                                 length=app.cols - long_side_width,
                                 y=split_rows, x=long_side_width,
                                 scroll=kwargs.get("scroll", False),
                                 border=border[2],
                                 border_style=border_styles[2])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]


def three_panels_horizontal(app, **kwargs):
    split_rows = int(app.rows / 2) - app.title_offset
    split_cols = int(app.cols / 2)
    long_side = kwargs.get("long_side", "top")
    border = kwargs.get("border", False)
    border_styles = kwargs.get("border_styles", [0, 0, 0])
    if isinstance(border, bool):
        border = [border] * 3
    long_side_height = kwargs.get("long_side_height", None)
    if not long_side_height:
        long_side_height = split_rows
    if long_side == "top":
        win1, panel1 = app.panel(height=long_side_height,
                                 length=app.cols,
                                 scroll=kwargs.get("scroll", False),
                                 y=0, x=0, border=border[0],
                                 border_style=border_styles[0])
        win2, panel2 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", False),
                                 y=long_side_height, x=0, border=border[1],
                                 border_style=border_styles[1])
        win3, panel3 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", False),
                                 y=long_side_height, x=split_cols,
                                 border=border[2],
                                 border_style=border_styles[2])
    elif long_side == "bottom":
        win1, panel1 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", False),
                                 y=0, x=0, border=border[0],
                                 border_style=border_styles[0])
        win2, panel2 = app.panel(height=app.rows - long_side_height,
                                 length=split_cols,
                                 scroll=kwargs.get("scroll", False),
                                 y=0, x=split_cols, border=border[1],
                                 border_style=border_styles[1])
        win3, panel3 = app.panel(height=long_side_height, length=app.cols,
                                 y=app.rows - long_side_height, x=0,
                                 scroll=kwargs.get("scroll", False),
                                 border=border[2],
                                 border_style=border_styles[2])
    curses.panel.update_panels()
    app.screen.refresh()
    app.panel_coords = [[0, 0], [0, 0], [0, 0]]
    app.panel_dimensions = [win1.getmaxyx(), win2.getmaxyx(),
                            win3.getmaxyx()]
    return [win1, win2, win3, panel1, panel2, panel3]
