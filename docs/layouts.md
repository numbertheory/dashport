# Layouts

Layouts in Dashport can be used to divide the screen easily and make separate panels that you can use `print` to display
text on.

In the [split_screen_quad example](https://github.com/numbertheory/dashport/blob/main/examples/layouts/split_screen_quad.py) the `split_screen_quad` method is done on the app, with `borders` enabled. You can then print to these panels, by passing in a "panel" string value to the print command. Each screen can only have one layout at a time, which the app stores in the app.panels dict under the key "layout".  

Using the `print` command, select the panel, by passing in a string which tells both that print should access the "layout" key to find the panel, and the index value of the panel that should be manipulated.  Example:

```
app.print("some text", panel="layout.0")
```
This would print `some text` to the first panel of the layout.

By default, the starting position of each panel is at `[0, 0]`, but you can manually set x and y to whatever position you need. Important note: the coordinates in each panel are relative to the panel, not the entire screen. Use the `panel_dimensions` attribute of each panel to evaluate the current maximum columns and rows that are available in each panel. The `panel_dimensions` attribute is a list of tuples, which give the dimensions of each panel.

```
#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap

def dashport(stdscr):
    app = Dashport(stdscr, color_default=176)
    app.add_control("q", quit, case_sensitive=False)
    app.split_screen_quad(borders=True)
    app.print("panel 0", panel="layout.0")
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2, panel="layout.0")
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3, panel="layout.0")
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

Other available splits are `split_screen_columns`, which divides the screen in two equal pieces, divided vertically, and `split_screen_rows` which does the same split with the division being horizontal.

## borders

You can also pass in a list of booleans into any layout to enable borders. Do this if you want some panels to have their border enabled, and some not. You can still just pass in a single boolean (not in a list), to enable borders on all panels.

```
    app.split_screen_quad(borders=[False, False, False, True])
```

## border_styles

The border_styles attribute can also be used to define the border styles of the individual panels. For this, provide a list of numbered border styles (see table below for the complete list of built-in border styles) that matches the panels that will be generated. Even if some panels don't have borders (in the example below, the second panel does not have a border), still place a value for the border style as a placeholder.

```
app.split_screen_quad(border=[True, False, True, True],
                      border_styles=[0, 1, 1, None])
app.panels["layout"][3].border('M', 'M', '=', '=', ' ', ' ', ' ', ' ')
```

By using `None` as a border style, the built-in borders are not used, and the program can then manually provide a border style, using the [native curses method](https://docs.python.org/3/library/curses.html#curses.window.border). The panels are all in the `app.panels` attribute as a list, so borders can be set manually for any panel that exists. To disable a border you've created manually, simply define that section of the border with a space character.

| border_styles # | Definition |
|-----------------| -------------|
| 0 | Default borders provided by curses `.border()` method |            |
| 1 | dashes and pluses `('\|', '\|', '-', '-', '+', '+', '+', '+')` |
| 2 | slashes no corners `('\\', '/', '=', '=', ' ', ' ', ' ', ' ')` |

# Three way splits

Splitting the screen in three ways means that you can determine which side of the screen the longer panel will be on (top or bottom for horizontal splits and left or right for vertical splits), and what the width of that panel will be.

When using `split_screen_three_vert`, set `long_side` to `left` or `right` to set the longer panel to the left or right, and then `long_side_width` to set the width of that panel. The other two panels will fill the screen to compensate. See [split_screen_three_vert.py](https://github.com/numbertheory/dashport/blob/main/examples/layouts/split_screen_three_vert.py) for an example.

When using `split_screen_three_horizontal`, set `long_side` to `top` or `bottom` to set the longer panel to the top or bottom, and then `long_side_height` to set the height of that panel. The other two panels will fill the screen to compensate. See [split_screen_three_horizontal.py](https://github.com/numbertheory/dashport/blob/main/examples/layouts/split_screen_three_horizontal.py) for an example.
