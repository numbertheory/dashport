# Buttons

Buttons are small areas of the screen that can be selected, clicked, and have actions associated with them. The [using_buttons.py](../examples/boilerplate/using_buttons.py) example in the `boilerplate` directory shows a basic usage of buttons. By design, buttons are more structured and less customizable than regular panels, but they allow applications to define lots of functionality in a minimal amount of code.

# Defining a Button

Buttons can be defined with a simple [widget](/widgets.md) command, like so. This button has no commands associated with it, and takes in a height, width, position (x, y), and color (see [colors.md](/colors.md) for using `<color>_on_<color>` syntax).

When a button is set to selected, the color for the button is reversed, to show the user which button is selected.

```
app.widget("button", button_name="quick", 
           color="default_on_blue",
           text="quick",
           x=1, y=1, height=5, width=13)
```

# Selecting a button

Using logic defined in your program, you can set up a control to cycle through the buttons on the screen in your program. In this example, the tab key, `\t`, is set as the key to cycle through buttons, but your own program could use whatever keys are necessary for your program.

As the program cycles through the selection, the `selected` option for each button widget is set to `True` or `False`. 

```
from dashport.dash import Dashport
from dashport.run import wrap


def quit(app):
    exit(0)

def cycle_buttons(app):
    button_names = ["quick", "brown", "fox"]
    next_index = button_names.index(app.selected_button) + 1
    if next_index == 3:
        next_index = 0
    app.selected_button = button_names[next_index]
    selection = [False, False, False]
    selection[next_index] = True
    app.widget("button", button_name="quick", 
               color="default_on_blue",
               text="quick",
               x=1, y=1, height=5, width=13, selected=selection[0])
    app.widget("button", button_name="brown",
               color="default_on_blue", text="brown", 
               x=1, y=7, height=5, width=13, selected=selection[1])
    app.widget("button", button_name="fox",
               color="default_on_blue", text="fox", 
               x=1, y=13, height=5, width=13, selected=selection[2])


def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit, case_sensitive=False)
    app.add_control("\t", cycle_buttons, case_sensitive=False)
    app.layout("single_panel", border=True)
    app.print("Button activation demo", x=1, y=1, panel="output.0")
    app.selected_button = "fox"
    cycle_buttons(app)
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport)

```

# Definining actions

Actions are defined using two options in the button widget, the `action` and `action_key` or `action_keys`. For each button you
want to perform an action, set `action` to a function you can pass through to the button, and set `action_keys` to the keys that will cause the action to be performed when that button is selected. 

In the example below, the `action_keys` are set to the `ENTER` key on the numeric keypad and the `ENTER` key (carriage return) on the keyboard for both buttons. This won't cause a conflict, because the button will only activate the action for the button that happens to be selected at the time.


```
    app.widget("button", button_name="quick", 
           color="default_on_blue",
           text="quick",
           action=quick_output_panel, action_keys=["\n", "KEY_ENTER"],
           x=1, y=1, height=5, width=13, selected=selection[0])
    app.widget("button", button_name="brown",
           color="default_on_blue", text="brown", 
           action=brown_output_panel, action_keys=["\n", "KEY_ENTER"],
           x=1, y=7, height=5, width=13, selected=selection[1])
```

This is so that you can define common ways for the user to activate a button, without having to define a different control for each individual button.

See [using_buttons.py](../examples/boilerplate/using_buttons.py) for the full example referenced in this documentation.