# layouts

Layouts in Dashport can be used to divide the screen easily and make separate panels that you can use `print` to display
text on.

In the [split_screen_quad example](examples/split_screen_quad.py) the `split_screen_quad` method is done on the app, with `borders` enabled. You can then print to these panels, by passing in a "panel" value to the print command. By default, the starting position of each panel is at `[0, 0]`, but you can manually set x and y to whatever position you need. Important note: the coordinates in each panel are relative to the panel, not the entire screen.

Other available splits are `split_screen_columns`, which divides the screen in two equal pieces, divided vertically, and `split_screen_rows` which does the same split with
