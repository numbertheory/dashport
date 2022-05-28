# layouts

Layouts in Dashport can be used to divide the screen easily and make separate panels that you can use `print` to display
text on.

In the [split_screen_quad example](examples/split_screen_quad.py) the `split_screen_quad` method is done on the app, with `borders` enabled. You can then print to these panels, by passing in a "panel" value to the print command. By default, the starting position of each panel is at `[0, 0]`, but you can manually set x and y to whatever position you need. Important note: the coordinates in each panel are relative to the panel, not the entire screen. Use the `panel_dimensions` attribute of each panel to evaluate the current maximum columns and rows that are available in each panel. The `panel_dimensions` attribute is a list of tuples, which give the dimensions of each panel.

```
#!/usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap

def dashport(stdscr):
    app = Dashport(stdscr, color_default=176)
    app.add_control("q", quit, case_sensitive=False)
    app.split_screen_quad(borders=True)
    app.print("panel 0", panel=0)
    app.print(f"Rows: {app.panel_dimensions[0][0]}", x=5, y=2, panel=0)
    app.print(f"Columns: {app.panel_dimensions[0][1]}", x=5, y=3, panel=0)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

Other available splits are `split_screen_columns`, which divides the screen in two equal pieces, divided vertically, and `split_screen_rows` which does the same split with the division being horizontal.

# Three way splits

Splitting the screen in three ways means that you can determine which side of the screen the longer panel will be on (top or bottom for horizontal splits and left or right for vertical splits), and what the width of that panel will be.

When using `split_screen_three_vert`, set `long_side` to `left` or `right` to set the longer panel to the left or right, and then `long_side_width` to set the width of that panel. The other two panels will fill the screen to compensate. See [split_screen_three_vert.py](examples/split_screen_three_vert.py) for an example.

When using `split_screen_three_horizontal`, set `long_side` to `top` or `bottom` to set the longer panel to the top or bottom, and then `long_side_height` to set the height of that panel. The other two panels will fill the screen to compensate. See [split_screen_three_horizontal.py](examples/split_screen_three_horizontal.py) for an example.
