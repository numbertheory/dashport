#! /usr/bin/env python3


def style(panel, border_style):
    if border_style == 0:
        panel.border()
    elif border_style == 1:
        panel.border('|', '|', '-', '-', '+', '+', '+', '+')
