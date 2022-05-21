#! /usr/bin/env python3
import curses
import dashport.commands as commands


class Dashport():
    def __init__(self, stdscr, **kwargs):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.window = curses.newwin(self.rows + 1, self.cols)
        self.controls = kwargs.get("keys")

    def refresh(self):
        key_pressed = self.screen.getkey()
        if key_pressed and self.controls:
            if key_pressed in self.controls:
                getattr(commands, self.controls[key_pressed])(self.screen)
        self.screen.refresh()
