#! /usr/bin/env python3
import curses
import curses.panel
from dashport.colors import color_pair_integer as cpi
from dashport.colors import color_defs
from dashport import layout


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
        self.cursor = self.curs_set(kwargs.get("cursor", 0))
        self.rows, self.cols = self.screen.getmaxyx()
        self.window = curses.newwin(self.rows + 1, self.cols)
        self.controls = dict()
        self.cursor_x = 0
        self.cursor_y = 0
        self.color_default = kwargs.get("color_default", 8)
        self.panels = []
        self.panel_dimensions = []
        curses.start_color()
        curses.use_default_colors()
        color_defs()

    def curs_set(self, set_cursor):
        curses.curs_set(set_cursor)

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

    def panel(self, height, length, y, x, border=False):
        win = curses.newwin(height, length, y, x)
        if border:
            win.box()
        panel = curses.panel.new_panel(win)
        curses.panel.update_panels()
        return win, panel

    def refresh(self):
        curses.panel.update_panels()
        self.control_keys()
        self.screen.refresh()

    def print(self, content="",  color=None, **kwargs):
        """
        Print behaves like a TTY print function. At the end of the content
        string the cursor goes to the next line by default.
        """
        set_y = kwargs.get("y", self.cursor_y)
        set_x = kwargs.get("x", self.cursor_x)
        panel = kwargs.get("panel")
        ending = kwargs.get("end", "\n")
        if not color:
            color = self.color_default
        if not isinstance(panel, int):
            self.screen.addstr(set_y, set_x, content,
                               cpi(self.color_default, color))
            if ending == "\n" and (
                set_y == self.cursor_y and
                    set_x == self.cursor_x):
                self.cursor_y += 1
        else:
            panel_y = kwargs.get("y", self.panel_coords[panel][1])
            panel_x = kwargs.get("x", self.panel_coords[panel][0])
            self.panels[panel].addstr(panel_y, panel_x, content,
                                      cpi(self.color_default, color))
            curses.panel.update_panels()
            self.screen.refresh()
            if ending == "\n" and (
                panel_y == self.panel_coords[panel][1] and
                    panel_x == self.panel_coords[panel][0]):
                self.panel_coords[panel][1] += 1

    def insstr(self, char="", x=None, y=None, color=None):
        """
        Add a character to the cursor position of the screen [x, y].
        Best used when you don't want the cursor to advance right when
        a character is placed.

        If no cursor position is specified, the current cursor position
        is used.
        """
        if not x:
            x = self.cursor_x
        if not y:
            y = self.cursor_y
        if not color:
            color = self.color_default
        self.screen.insstr(y, x, char, cpi(self.color_default, color))

    def addstr(self, content, x, y, color=None):
        """
        Adds a string to the location specified by x, y coordinates. Similar
        to this class's print method, but with no shifting of content already
        on the screen, and the cursor position does not move.
        """
        if not color:
            color = self.color_default
        self.screen.addstr(y, x, content, cpi(self.color_default, color))

    def rectangle(self, x, y, width, height, color=None):
        """
        Draw a filled in rectangle on the screen.
        """
        for j in range(y, y + height):
            for i in range(x, x + width):
                self.screen.addstr(j, i, " ", cpi(self.color_default, color))

    def background(self, color):
        """
        Fill the background with a color
        """
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.screen.insstr(j, i, " ", cpi(self.color_default, color))

    def split_screen_columns(self, **kwargs):
        """
        Splits the screen into two vertical panels
        """
        self.panels = layout.split_screen_columns(
            self, kwargs.get("borders", False))

    def split_screen_rows(self, **kwargs):
        """
        Splits the screen into two horizontal panels
        """
        self.panels = layout.split_screen_rows(
            self, kwargs.get("borders", False))

    def split_screen_quad(self, **kwargs):
        """
        Splits the screen into four quadrant panels
        """
        self.panels = layout.quadrants(
            self, kwargs.get("borders", False))

    def split_screen_three(self, **kwargs):
        """
        Splits the screen into three panels
        """
        self.panels = layout.three_panels_vert(
            self, kwargs.get("borders", False))
