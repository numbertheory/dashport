# Using Dashport

This the [boilerplate](https://github.com/numbertheory/dashport/blob/main/examples/boilerplate/boilerplate.py) code that can be used to start any application. This code won't display anything, it will just set up a curses screen, and continually refresh until the user uses Ctrl+C to break out of it. See documentation below for details on building on this boilerplate.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

# This info function displays a better error message if
# the program crashes.
def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr)

    # This loop refreshes the screen. Put commands in this loop if you
    # want them to be refreshed every millisecond.
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

## Dashport App Options

When making a dashport app, you can hide the cursor, by setting the cursor to `False`. If you need to set the cursor back to visible during the program, use the `curs_set` method to bring it back.

```
def dashport(stdscr):
    app = Dashport(stdscr, cursor=False)
    # bring the cursor back
    app.curs_set(True)
```

## Printing Statements

Dashport contains its own print function, which is separate from Python's `print` command. To use the method, just add the method to the dashport function, as shown below.

```
def dashport(stdscr):
    app = Dashport(stdscr)
    app.print("Some text is on the screen!", x=0, y=10)
    while True:
        app.refresh()
```

The coordinate system in Dashport is `x` refers to the horizontal position (the column on the screen), and y refers to the (the row on the screen).

See [Add String Methods](strings.md) for more information and other methods to add characters to your app's screen.

## Coordinate layout
If you are familiar with the built-in Python curses library, you'll note that `x` and `y` for Dashport is switched, so that `x` refers to columns and `y` refers to rows. The origin `(0, 0)` is still the top-left of the screen, and values increase for `x` as you move right and increase for `y` as you move down the screen. Run the [explore_screen.py](https://github.com/numbertheory/dashport/blob/main/examples/util/explore_screen.py) example to see this in action.

This was done to make the coding experience a bit more approachable, so you can use the values of the size of the screen itself (`app.rows`, `app.cols`) to figure out the limits of whether or not a string or character can be placed.

## Binding keys to the application

We probably want to make a quit command so that we can quit the program without having to press Ctrl+C.  To do that, use the add_control method in the dashport function:

```
def quit(*args):
    exit(0)

def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit, case_sensitive=False)
    ...
```
The first argument is a string, the key that is being bound. The second argument is the function itself, which will be added to the `app.controls` dict of the app we've defined. And finally, you can set an optional `case_sensitive` argument to `False`, if you would like both upper and lowercase versions of the key pressed to be bound to the same function.

In this example, the `q` key is bound to the quit function, which you can define yourself outside of the dashport function. You can also import functions from other python files or libraries, and bind those functions to other keys. Even if a function takes no arguments, the function still needs `*args` set. If you want your function to interact with the screen and have access to other Dashport functions, pass in "app" into the function:

In this example, the add_message function is bound to the `k` key. When pressed, the app will display the new message on the screen.

```
def add_message(app):
    app.print("A new message appears!")

def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("k", add_message)
    ...
```

## Native curses methods

Because this is a wrapper, and a work in progress, not all functions in curses will be implemented, but you may still use curses methods in your applications set up by Dashport. The `screen` attribute in the Dashport object is just defined as the curses object, so you can use [any documented curses method](https://docs.python.org/3/library/curses.html) with it.

In the example below, `addstr` is being used, but it's not the `addstr` method in Dashport, it's the `addstr` method native to curses, and so it takes different arguments.

```
def dashport(stdscr):
    app = Dashport(stdscr)
    app.screen.addstr(10, 10, "k")
    ...
```
