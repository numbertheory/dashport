# String Methods

## insstr

The insstr (insert string) method is used when a character should be placed directly at the current cursor position without the cursor moving. If your operation requires a character to be placed in a corner of the screen, it's best to use insstr so that placing the character doesn't cause the cursor to move to the right by one and crash your program.

In the example below, this will place your character at the bottom left corner of the screen, regardless of the size of the terminal window.

```
def dashport(stdscr):
    app = Dashport(stdscr)
    app.instr("X", x=0, y=app.rows - 1)
    ...
```

## addstr

The addstr method adds all the characters of a string to the x, y position.

```
def dashport(stdscr):
    app = Dashport(stdscr)
    app.addstr("This string overwrites all other content", x=0, y=app.rows - 1)
    ...
```

## print

This method is meant to be close in function to Python's print method and lets you mimic a TTY on a curses screen. Like `addstr`, it will add characters to the screen, but unlike `addstr`, it will also move the cursor down by one y-coordinate to simulate a carriage return. You may opt to turn this behavior for a print statement off by passing in an `end` option, to override the default, but if that's your use case you may want to use `addstr` instead.

Like addstr, it can take `x` and `y` coordinates, but when that is implemented,
the next print statement would follow below the previous print statement that
had no `x` and `y` coordinates set.

```
def dashport(stdscr):
    app = Dashport(stdscr)
    app.print("This string overwrites all other content")
    app.print("This is in a different location.", x= 10, y=15, end=False)
    app.print("This is on the next line.")
    ...
```
