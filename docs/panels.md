# Panels

Panels that split and take up the entire screen are created automatically with [layouts](/layouts.md). Using layouts, panels are created inside the main Dashport object, in the `panels` dictionary, under the layouts key. To refer to a single panel in a layout, use the `panel` option in the `print` or `background` command:

```
app.background(color="red_on_white", panel="layout.0")
app.print("This is the first panel in the layout.", x=5, y=2, panel="layout.0")

``` 

You can also create arbitrarily sized panels in your application.  You'll use the `panel` method on the app to create the
panel, and store it in the panels dictionary, without overriding the layout. You can use the same border options that exist
for layout when definining them, and the same method to refer to them when using `print` or `background`.

```
app.panels["some_panel"] = app.panel(height=3, width=25, y=20, x=20, border=True, border_style=3)
app.print("this is another panel", x=1, y=1, panel="some_panel.0")
```
