#! /usr/bin/env python3
from curses import wrapper
import curses


class Dashport():
    def __init__(self, stdscr):
        self.screen = stdscr
        self.window = curses.newwin(self.screen.rows + 1, self.screen.cols)

    def main(self):
        self.screen.refresh()

    def run(self):
        wrapper(self.main)
