#! /usr/bin/env python3
import curses


def style(panel, border_style=None, **kwargs):
    if border_style == 0:
        panel.border(curses.ACS_VLINE,
                     curses.ACS_VLINE,
                     curses.ACS_HLINE,
                     curses.ACS_HLINE,
                     curses.ACS_ULCORNER,
                     curses.ACS_URCORNER,
                     curses.ACS_LLCORNER,
                     curses.ACS_LRCORNER)
    elif border_style == 1:
        panel.border('|', '|', '-', '-', '+', '+', '+', '+')
    elif border_style == 2:
        panel.border('\\', '/', '=', '=', ' ', ' ', ' ', ' ')
