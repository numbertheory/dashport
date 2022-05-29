#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def quit(*args):
    exit(0)


def move_up(app):
    app.screen.clear()
    if app.cursor_y != 0:
        app.cursor_y -= 1


def move_down(app):
    app.screen.clear()
    if app.rows - 1 > app.cursor_y:
        app.cursor_y += 1


def move_left(app):
    app.screen.clear()
    if app.cursor_x != 0:
        app.cursor_x -= 1


def move_right(app):
    app.screen.clear()
    if app.cols - 1 > app.cursor_x:
        app.cursor_x += 1


def dashport(stdscr):
    app = Dashport(stdscr, cursor=False)
    app.add_control("q", quit)
    app.add_control("KEY_UP", move_up)
    app.add_control("KEY_DOWN", move_down)
    app.add_control("KEY_LEFT", move_left)
    app.add_control("KEY_RIGHT", move_right)
    while True:
        app.insstr("X")
        app.addstr("Position: {} {}".format(app.cursor_x, app.cursor_y),
                   x=0, y=app.rows - 1, color=4)
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
