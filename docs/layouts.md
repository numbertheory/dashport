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
