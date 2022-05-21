#! /usr/bin/env python3
import curses


class Dashport():
    def __init__(self, stdscr):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.window = curses.newwin(self.rows + 1, self.cols)

    def refresh(self):
        self.screen.refresh()
