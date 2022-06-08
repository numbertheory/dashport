# Widgets

## title_bar

The title bar widget occupies one row on either the top or bottom of the screen to display persistent information. The title bar does
take away one row from the screen, so even if a `print` command designates a spot where the title bar is, those coordinates will not
overlap with the title_bar.

Example:

```
#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr)
    app.widget("title_bar", text="This is the title bar", color=256)
    app.print(content="this is text", x=0, y=0)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)


```
