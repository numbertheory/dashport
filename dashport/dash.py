#! /usr/bin/env python3
import curses
import dashport.commands as commands


class Info():
    def __init__(self, stdscr, **kwargs):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.cursor_y = 0
        self.cursor_x = 0

    def print(self, content="", **kwargs):
        set_y = kwargs.get("y", self.cursor_y)
        set_x = kwargs.get("x", self.cursor_x)
        ending = kwargs.get("end", "\n")
        self.screen.addstr(set_y, set_x, content)
        if ending == "\n":
            self.cursor_y += 1


class Dashport():
    def __init__(self, stdscr, **kwargs):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.window = curses.newwin(self.rows + 1, self.cols)
        self.controls = dict()
        self.cursor_x = 0
        self.cursor_y = 0

    def add_control(self, control_key, func, case_sensitive=True):
        """
        Binds a keyboard key to a function in the program.
        :param control_key: The string of the key that will be
                           bound to the function.
        :param func: The function that will be executed when
                    this key is pressed
        :param case_sensitive: If set to ``False`` this will add both
                               upper and lowercase characters of the
                               control_key to the same function
        """
        if case_sensitive:
            self.controls[control_key] = func
        if not case_sensitive:
            self.controls[control_key.upper()] = func
            self.controls[control_key.lower()] = func

    def control_keys(self):
        key_pressed = self.screen.getkey()
        if key_pressed and self.controls:
            if key_pressed in self.controls:
                self.controls[key_pressed](self)

    def refresh(self):
        self.control_keys()
        self.screen.refresh()

    def print(self, content="", **kwargs):
        set_y = kwargs.get("y", self.cursor_y)
        set_x = kwargs.get("x", self.cursor_x)
        ending = kwargs.get("end", "\n")
        self.screen.addstr(set_y, set_x, content)
        if ending == "\n":
            self.cursor_y += 1
