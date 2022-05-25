## colors

Color text in curses is usually done via a `color_pairs` method. With Dashport, color pairs (foreground and background) are defined with a single integer which sets both backgrounnd and foreground.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

def info(stdscr):
    return Info(stdscr)

def dashport(stdscr):
    app = Dashport(stdscr)
    app.print("some color text", x=20, color=3)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

Use this table to find the color scheme appropriate for your app:

![color palette for dashport](docs/color_palette.png?raw=true "Dashport Color Palette")
