# Colors

Color text in curses is usually done via a `color_pairs` method. With Dashport, color pairs (foreground and background) are defined with a single string which sets both background and foreground using plain English words connected by the string `_on_`. So, if you want red text on a white background, the color definition would be `red_on_white`.

Set the `color_default` value when starting a Dashport object to set the default text color value. Setting the color_default to `None` will set the default color to the default colors of the terminal session.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

def info(stdscr):
    return Info(stdscr)

def dashport(stdscr):
    app = Dashport(stdscr, color_default="green_on_white")
    app.print("hello world", color="red_on_white")
    app.print("plain text, colored with color_default")
    app.print("black on blue text", color="black_on_blue")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)

```



The `background` method will fill the background with the background for the `color` selected. It does this by setting down a space character in every text position. It's best to use background before any other printing commands.

Use the `rectangle` method to draw a rectangle. It's best to keep rectangles away from the edges or corners of the screen, or filling up the entire screen. Use `background` to fill the screen with a color, or insstr to insert a string into the corner.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

def info(stdscr):
    return Info(stdscr)

def dashport(stdscr):
    app = Dashport(stdscr, color_default="yellow_on_blue")
    app.print("this text won't show")
    app.background(color="white_on_maroon")
    app.print("some color text", x=20, color="blue_on_yellow")
    app.rectangle(10, 10, 12, 12, color="blue_on_yellow")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

## Default Color Definitions

In Python's implementation of curses there are 255 color pair positions available to define colors, and by default, Dashport uses those color pairs for color definitions. These are the colors Dashport defines. Run the `examples/util/color_palette.py` program in the examples folder for an interactive guide in showing how all the colors will look on your screen:

- default
- black
- maroon
- green
- olive
- navy
- purple
- teal
- silver
- grey
- red
- lime
- yellow
- blue
- fuchsia
- aqua
- white

Whenever a Dashport command, like `print`, uses a `color` argument, you can use the standard `<color>_on_<color>` formatted string to define the foreground and background. 

```
# This creates blue color text with a yellow background.
app.print("some color text", color="blue_on_yellow")
```

Due to the limit of 255 color pairs, the `olive` and `teal` colors are not available as background colors, but you can still use them as background colors, simply by formatting them with an A_REVERSE argument in the print command:

```
# This creates black text on an olive background.
app.print("some color text", color="olive_on_black", A_REVERSE=True)
```

# Defining your own color definitions with curses

You can still use regular color pairs you've defined in curses, if you want to get an exact color. When initiating Dashport, set the color_map option to False, and then create color pairs just as you would with the normal curses library. You can still use Dashport's `print` and other string commands, passing in the integer of the color pair you've defined, rather than a string.

```
from dashport.dash import Dashport
from dashport.run import wrap
import curses

def dashport(stdscr):
    app = Dashport(stdscr, color_map=False)
    curses.init_pair(1, 2, 4)
    app.print("plain text")
    app.print("plain text, colored with a curses color pair", color=1)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)

```


# Formatting text

The `print` function can take various attributes to change the text. These text attributes are available in the [Python curses documentation](https://docs.python.org/3/library/curses.html#curses.ncurses_version). Use the constants listed in the table to change the text. In the example below, `A_BOLD` is set, which boldens the text. Please note, that support for these attributes is very system-dependent, and some attributes may not be available on all systems. Any unavailable text formatting will be ignored by Dashport, rather than crash the program.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

def info(stdscr):
    return Info(stdscr)

def dashport(stdscr):
    app = Dashport(stdscr, color_default="green_on_white")
    app.print("This text is bold.", A_BOLD=True)
    app.print("This text is italic.", A_ITALIC=True)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```
