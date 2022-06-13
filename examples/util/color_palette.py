#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap
from dashport.characters import BoxDrawing

"""
This demo needs at least 110 columns and 40 lines to work.
"""


def set_range(app, custom_range):
    app.cursor_y = 0
    color_names = list(app.color_names.keys())
    app.widget("title_bar", text="Color Palette Test Application".center(app.cols, " "), color="white_on_red")
    app.layout("split_screen_columns", border=[False, True], center_divide_x=21)
    app.print("FORMATS".center(20, " "), x=0, y=18, panel="layout.0", color="black_on_white")
    app.print("press F to change", x=0, y=19, panel="layout.0")
    format_list_y = 20
    for format_style in ["Appearance", "Highlights", "Others"]:
        if app.format_cycle == format_style.lower():
            app.print(f"> {format_style}", x=0, y=format_list_y, panel="layout.0", color="black_on_white")
        else:
            app.print(f"  {format_style}", x=0, y=format_list_y, panel="layout.0")
        format_list_y += 1
    app.panels["layout"][1].clear()
    app.print("BACKGROUND".center(20, " "), x=0, y=0, panel="layout.0", color="black_on_white")
    app.print(BoxDrawing.char("double_horizontal") * 20, x=0, y=1, panel="layout.0")
    panel_list_y = 2
    for background in app.color_backgrounds:
        if background == app.selected_background:
            app.print(f">{background}".ljust(20), x=0, y=panel_list_y, panel="layout.0", A_REVERSE=True)
        else:
            app.print(f"{background}", x=1, y=panel_list_y, panel="layout.0")
        panel_list_y += 1
    if app.format_cycle == "appearance":
        app.print("A_NORMAL", x=1, y=1, panel="layout.1")
        app.print("A_REVERSE", x=22, y=1, panel="layout.1")
        app.print("A_BOLD", x=44, y=1, panel="layout.1")
        app.print("A_ITALIC", x=66, y=1, panel="layout.1")
        app.print("A_DIM", x=1, y=20, panel="layout.1")
        app.print("A_UNDERLINE", x=22, y=20, panel="layout.1")
        app.print("A_BLINK", x=44, y=20, panel="layout.1")
        app.print("A_INVIS", x=66, y=20, panel="layout.1")
        for j in range(custom_range[0], custom_range[1]):
            app.print(f"{color_names[j]}", x=1, y=app.cursor_y + 2, color=color_names[j], panel="layout.1")
            app.print(f"{color_names[j]}", x=22, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_REVERSE=True)
            app.print(f"{color_names[j]}", x=44, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_BOLD=True)
            app.print(f"{color_names[j]}", x=66, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_ITALIC=True)
            app.print(f"{color_names[j]}", x=1, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_DIM=True)
            app.print(f"{color_names[j]}", x=22, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_UNDERLINE=True)
            app.print(f"{color_names[j]}", x=44, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_BLINK=True)
            app.print(f"{color_names[j]}", x=66, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_INVIS=True)
            app.cursor_y += 1

    if app.format_cycle == "highlights":
        app.print("A_VERTICAL", x=1, y=1, panel="layout.1")
        app.print("A_HORIZONTAL", x=22, y=1, panel="layout.1")
        app.print("A_LEFT", x=44, y=1, panel="layout.1")
        app.print("A_LOW", x=1, y=20, panel="layout.1")
        app.print("A_RIGHT", x=22, y=20, panel="layout.1")
        app.print("A_TOP", x=44, y=20, panel="layout.1")
        for j in range(custom_range[0], custom_range[1]):
            app.print(f"{color_names[j]}", x=1, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_VERTICAL=True)
            app.print(f"{color_names[j]}", x=22, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_HORIZONTAL=True)
            app.print(f"{color_names[j]}", x=44, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_LEFT=True)
            app.print(f"{color_names[j]}", x=1, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_LOW=True)
            app.print(f"{color_names[j]}", x=22, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_RIGHT=True)
            app.print(f"{color_names[j]}", x=44, y=app.cursor_y + 21, color=color_names[j], panel="layout.1",
                      A_TOP=True)
            app.cursor_y += 1

    if app.format_cycle == "others":
        app.print("A_ALTCHARSET", x=1, y=1, panel="layout.1")
        app.print("A_PROTECT", x=22, y=1, panel="layout.1")
        app.print("A_CHARTEXT", x=44, y=1, panel="layout.1")
        for j in range(custom_range[0], custom_range[1]):
            app.print(f"{color_names[j]}", x=1, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_ALTCHARSET=True)
            app.print(f"{color_names[j]}", x=22, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_PROTECT=True)
            app.print(f"{color_names[j]}", x=44, y=app.cursor_y + 2, color=color_names[j], panel="layout.1",
                      A_CHARTEXT=True)
            app.cursor_y += 1


def default_range(app):
    set_range(app, [1, 17])


def next_background(app):
    backgrounds = list(app.color_backgrounds.keys())
    if app.selected_background != "purple":
        current_index = backgrounds.index(app.selected_background)
        app.selected_background = backgrounds[current_index+1]


def prev_background(app):
    backgrounds = list(app.color_backgrounds.keys())
    if app.selected_background != "default":
        current_index = backgrounds.index(app.selected_background)
        app.selected_background = backgrounds[current_index - 1]


def cycle_format(app):
    cycle_formats = ["appearance", "highlights", "others"]
    current_index = cycle_formats.index(app.format_cycle)
    if current_index < 2:
        app.format_cycle = cycle_formats[current_index + 1]
    else:
        app.format_cycle = cycle_formats[0]



def white_range(app):
    set_range(app, [17, 34])


def black_range(app):
    set_range(app, [34, 51])


def silver_range(app):
    set_range(app, [51, 68])


def grey_range(app):
    set_range(app, [68, 85])


def red_range(app):
    set_range(app, [85, 102])


def lime_range(app):
    set_range(app, [102, 119])


def yellow_range(app):
    set_range(app, [119, 136])


def blue_range(app):
    set_range(app, [136, 153])


def fuchsia_range(app):
    set_range(app, [153, 170])


def aqua_range(app):
    set_range(app, [170, 187])


def maroon_range(app):
    set_range(app, [187, 204])


def green_range(app):
    set_range(app, [204, 221])


def navy_range(app):
    set_range(app, [221, 238])


def purple_range(app):
    set_range(app, [238, 255])


def exit_program(*args):
    exit(0)


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr, color_default=9)
    app.format_cycle = "appearance"
    app.add_control("q", exit_program, case_sensitive=False)
    app.add_control("F", cycle_format, case_sensitive=False)
    app.set_color_range = [1, 17]
    app.selected_background = "default"
    app.add_control("KEY_DOWN", next_background)
    app.add_control("KEY_UP", prev_background)
    while True:
        globals()["{}_range".format(app.selected_background)](app)
        app.refresh()



if __name__ == '__main__':
    wrap(dashport, info)
