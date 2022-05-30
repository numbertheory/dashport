#! /usr/bin/env python3
import curses
import curses.panel
from dashport.colors import color_pair_integer as cpi
from dashport.colors import color_defs
from dashport import layout, widgets


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
        self.title_bottom_offset = 0
        self.cursor = self.curs_set(kwargs.get("cursor", 0))
        self.rows, self.cols = self.screen.getmaxyx()
        self.window = curses.newwin(self.rows + 1, self.cols)
        self.controls = dict()
        self.cursor_x = 0
        self.cursor_y = 0
        self.color_default = kwargs.get("color_default", 8)
        self.panels = []
        self.panel_dimensions = []
        self.panel_scroll = []
        self.panel_border = []
        self.title_offset = 0
        self.top_title_row = None
        self.bottom_title_row = self.rows - 1
        self.scroll_screen = False
        if kwargs.get("scroll"):
            self.screen.scrollok(True)
            self.scroll_screen = True
        self.screen.setscrreg(0, self.rows - 1)
        curses.start_color()
        curses.use_default_colors()
        color_defs()

    def curs_set(self, set_cursor):
        curses.curs_set(set_cursor)

    def title_bar(self, **kwargs):
        text = kwargs.get("text", "")
        align = kwargs.get("align", "top")
        color = kwargs.get("color", self.color_default)
        widgets.title_bar(self, text=text, align=align, color=color)

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

    def panel(self, **kwargs):
        height = kwargs.get("height")
        length = kwargs.get("length")
        y = kwargs.get("y")
        x = kwargs.get("x")
        border = kwargs.get("border")
        enable_scroll = kwargs.get("scroll", False)
        win = curses.newwin(height, length, y + self.title_offset, x)
        if enable_scroll:
            win.scrollok(True)
            if border:
                win.setscrreg(1, height - 2)
            else:
                win.setscrreg(0, height - 1)
        if border:
            win.box()
        panel = curses.panel.new_panel(win)
        self.panel_border.append(border)
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
        set_y = kwargs.get("y", self.cursor_y) + self.title_offset
        set_x = kwargs.get("x", self.cursor_x)
        panel = kwargs.get("panel")
        ending = kwargs.get("end", "\n")
        if set_y == self.top_title_row:
            set_y += 1
        if set_y == self.bottom_title_row and self.scroll_screen:
            self.screen.scroll(1)
            ending = ""
        if not color:
            color = self.color_default
        if not isinstance(panel, int):
            self.screen.addstr(set_y, set_x, content,
                               cpi(self.color_default, color))
            if ending == "\n" and (
                set_y == self.cursor_y + self.title_offset and
                    set_x == self.cursor_x):
                self.cursor_y += 1
        else:
            panel_y = kwargs.get("y", self.panel_coords[panel][1])
            panel_x = kwargs.get("x", self.panel_coords[panel][0])
            if self.panel_border[panel]:
                border_offset = 2
            else:
                border_offset = 1
            if panel_y > self.panel_dimensions[panel][0] - border_offset:
                self.panels[panel].scroll(1)
                ending = ""
                panel_y = self.panel_dimensions[panel][0] - border_offset
            self.panels[panel].addstr(panel_y, panel_x, content,
                                      cpi(self.color_default, color))
            if self.panel_border[panel]:
                self.panels[panel].box()
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
            y = self.cursor_y + self.title_offset
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
        self.screen.addstr(y + self.title_offset, x, content,
                           cpi(self.color_default, color))

    def rectangle(self, x, y, width, height, color=None):
        """
        Draw a filled in rectangle on the screen.
        """
        for j in range(y + self.title_offset,
                       y + height - self.title_bottom_offset):
            for i in range(x, x + width):
                self.screen.addstr(j, i, " ", cpi(self.color_default, color))

    def background(self, color):
        """
        Fill the background with a color
        """
        for j in range(0 + self.title_offset,
                       self.rows - self.title_bottom_offset):
            for i in range(0, self.cols):
                self.screen.insstr(j, i, " ", cpi(self.color_default, color))

    def split_screen_columns(self, **kwargs):
        """
        Splits the screen into two vertical panels
        """
        self.panels = layout.split_screen_columns(
            self, border=kwargs.get("border", False),
            scroll=kwargs.get("scroll", False))

    def split_screen_rows(self, **kwargs):
        """
        Splits the screen into two horizontal panels
        """
        self.panels = layout.split_screen_rows(
            self, border=kwargs.get("border", False),
            scroll=kwargs.get("scroll", False))

    def split_screen_quad(self, **kwargs):
        """
        Splits the screen into four quadrant panels
        """
        self.panels = layout.quadrants(
            self, border=kwargs.get("border", False),
            scroll=kwargs.get("scroll", False))

    def split_screen_three_vert(self, **kwargs):
        """
        Splits the screen into three panels
        """
        self.panels = layout.three_panels_vert(
            self, border=kwargs.get("border", False),
            long_side=kwargs.get("long_side", "right"),
            long_side_width=kwargs.get("long_side_width"),
            scroll=kwargs.get("scroll", False))

    def split_screen_three_horizontal(self, **kwargs):
        """
        Splits the screen into three panels
        """
        self.panels = layout.three_panels_horizontal(
            self, border=kwargs.get("border", False),
            long_side=kwargs.get("long_side", "top"),
            long_side_height=kwargs.get("long_side_height"),
            scroll=kwargs.get("scroll", False))
