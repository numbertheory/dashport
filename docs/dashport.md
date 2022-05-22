# Using Dashport

This the [boilerplate](examples/boilerplate.py) code that can be used to start any application. This code won't display anything, it will just set up a curses screen, and continually refresh until the user uses Ctrl+C to break out of it. See documentation below for details on building on this boilerplate.

```
from dashport.dash import Dashport, Info
from dashport.run import wrap

# This info function displays a better error message if
# the program crashes.
def info(stdscr):
    return Info(stdscr)


def dashport(stdscr):
    app = Dashport(stdscr)

    # This loop refreshes the screen. Don't put any other commands
    # in this loop, instead add to the `app` object above, and let
    # this loop run.
    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)
```

## Binding keys to the application

The first thing we probably want to do is make a quit command so that we can quit the program without having to press Ctrl+C.  To do that, use the add_control method in the dashport function:

```
def quit():
    exit(0)

def dashport(stdscr):
    app = Dashport(stdscr)
    app.add_control("q", quit, case_sensitive=False)
    ...
```
The first argument is a string, the key that is being bound. The second argument is the function itself, which will be added to the `app.controls` dict of the app we've defined.

This will bind the `q` key to the quit function, which you can define yourself outside of the dashport function. You can also import functions from other python files or libraries, and bind those functions to the
