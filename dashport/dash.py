#! /usr/bin/env python3
import curses
import curses.panel
from dashport.colors import color_pair_integer as cpi
from dashport.colors import color_defs, format_text
from dashport import layout, widgets, borders


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
        self.panels = dict()
        self.panel_dimensions = []
        self.panel_scroll = []
        self.panel_border = []
        self.panel_border_styles = []
        self.title_offset = 0
        self.top_title_row = None
        self.bottom_title_row = self.rows - 1
        self.scroll_screen = False
        self.current_command = ""
        if kwargs.get("scroll"):
            self.screen.scrollok(True)
            self.scroll_screen = True
        self.screen.setscrreg(0, self.rows - 1)
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

    def panel(self, **kwargs):
        height = kwargs.get("height")
        length = kwargs.get("length")
        y = kwargs.get("y")
        x = kwargs.get("x")
        border = kwargs.get("border")
        border_style = kwargs.get("border_style", 0)
        enable_scroll = kwargs.get("scroll", False)
        win = curses.newwin(height, length, y + self.title_offset, x)
        if enable_scroll:
            win.scrollok(True)
            if border:
                win.setscrreg(1, height - 2)
            else:
                win.setscrreg(0, height - 1)
        if border:
            borders.style(win, border_style)
        panel = curses.panel.new_panel(win)
        self.panel_border.append(border)
        self.panel_border_styles.append(border_style)
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
        if kwargs.get("panel"):
            panel = [x for x in kwargs.get("panel").split(".")
                     if not x.isdigit()]
            panel.append(int(kwargs.get("panel").split(".")[1]))
        else:
            panel = None
        ending = kwargs.get("end", "\n")
        format_text_list = format_text(kwargs)
        if set_y == self.top_title_row:
            set_y += 1
        if set_y == self.bottom_title_row and self.scroll_screen:
            self.screen.scroll(1)
            ending = ""
        if not color:
            color = self.color_default
        if not isinstance(panel, list):
            self.screen.addstr(set_y, set_x, content,
                               cpi(self.color_default, color)
                               | format_text_list[0]
                               | format_text_list[1]
                               | format_text_list[2]
                               | format_text_list[3]
                               | format_text_list[4]
                               | format_text_list[5]
                               | format_text_list[6]
                               | format_text_list[7]
                               | format_text_list[8]
                               | format_text_list[9]
                               | format_text_list[10]
                               | format_text_list[11]
                               | format_text_list[12]
                               | format_text_list[13]
                               | format_text_list[14]
                               | format_text_list[15]
                               | format_text_list[16]
                               | format_text_list[17])
            if ending == "\n" and (
                set_y == self.cursor_y + self.title_offset and
                    set_x == self.cursor_x):
                self.cursor_y += 1
        else:
            panel_y = kwargs.get("y", self.panel_coords[panel[1]][1])
            panel_x = kwargs.get("x", self.panel_coords[panel[1]][0])
            if self.panel_border[panel[1]]:
                border_offset = 2
            else:
                border_offset = 1
            if panel_y > self.panel_dimensions[panel[1]][0] - border_offset:
                self.panels[panel[0]][panel[1]].scroll(1)
                ending = ""
                panel_y = self.panel_dimensions[panel[1]][0] - border_offset
            self.panels[panel[0]][panel[1]].addstr(
                panel_y, panel_x, content,
                cpi(self.color_default, color)
                | format_text_list[0]
                | format_text_list[1]
                | format_text_list[2]
                | format_text_list[3]
                | format_text_list[4]
                | format_text_list[5]
                | format_text_list[6]
                | format_text_list[7]
                | format_text_list[8]
                | format_text_list[9]
                | format_text_list[10]
                | format_text_list[11]
                | format_text_list[12]
                | format_text_list[13]
                | format_text_list[14]
                | format_text_list[15]
                | format_text_list[16]
                | format_text_list[17])
            if self.panel_border[panel[1]]:
                borders.style(self.panels[panel[0]][panel[1]],
                              self.panel_border_styles[panel[1]])
            curses.panel.update_panels()
            self.screen.refresh()

            if ending == "\n" and (
                panel_y == self.panel_coords[panel[1]][1] and
                    panel_x == self.panel_coords[panel[1]][0]):
                self.panel_coords[panel[1]][1] += 1

    def insstr(self, char="", x=None, y=None, color=None, **kwargs):
        """
        Add a character to the cursor position of the screen [x, y].
        Best used when you don't want the cursor to advance right when
        a character is placed.

        If no cursor position is specified, the current cursor position
        is used.
        """
        format_text_list = format_text(kwargs)
        if not x:
            x = self.cursor_x
        if not y:
            y = self.cursor_y + self.title_offset
        if not color:
            color = self.color_default
        self.screen.insstr(y, x, char, cpi(self.color_default, color)
                           | format_text_list[0]
                           | format_text_list[1]
                           | format_text_list[2]
                           | format_text_list[3]
                           | format_text_list[4]
                           | format_text_list[5]
                           | format_text_list[6]
                           | format_text_list[7]
                           | format_text_list[8]
                           | format_text_list[9]
                           | format_text_list[10]
                           | format_text_list[11]
                           | format_text_list[12]
                           | format_text_list[13]
                           | format_text_list[14]
                           | format_text_list[15]
                           | format_text_list[16]
                           | format_text_list[17])

    def addstr(self, content, x, y, color=None, **kwargs):
        """
        Adds a string to the location specified by x, y coordinates. Similar
        to this class's print method, but with no shifting of content already
        on the screen, and the cursor position does not move.
        """
        format_text_list = format_text(kwargs)
        if not color:
            color = self.color_default
        self.screen.addstr(y + self.title_offset, x, content,
                           cpi(self.color_default, color)
                           | format_text_list[0]
                           | format_text_list[1]
                           | format_text_list[2]
                           | format_text_list[3]
                           | format_text_list[4]
                           | format_text_list[5]
                           | format_text_list[6]
                           | format_text_list[7]
                           | format_text_list[8]
                           | format_text_list[9]
                           | format_text_list[10]
                           | format_text_list[11]
                           | format_text_list[12]
                           | format_text_list[13]
                           | format_text_list[14]
                           | format_text_list[15]
                           | format_text_list[16]
                           | format_text_list[17])

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

    def layout(self, layout_name, **kwargs):
        self.panels["layout"] = getattr(layout, layout_name)(self, **kwargs)

    def widget(self, widget_name, **kwargs):
        getattr(widgets, widget_name)(self, **kwargs)
