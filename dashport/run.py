#! /usr/bin/env python3
import curses
from curses import wrapper


def error_message(e, screen):
    print("Curses Error: {}".format(e))
    # Print debug info to stdout
    info = wrapper(screen)
    print("Curses crashed. It may be due to your terminal window "
          "being too small or referencing a position "
          "that does not exist. Here's the debug info:")
    print("# of rows: {}".format(info.rows))
    print("# of cols: {}".format(info.cols))


def wrap(dashport, info=None):
    try:
        wrapper(dashport)
    except curses.error as e:
        if info:
            error_message(e, info)
        else:
            print(e)
            raise
