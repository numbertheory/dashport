## basic_window

### Summary
Creates a basic window with a keyboard command to quit. Also demonstrates creating text on the screen.

### Details

The `keys` value you pass into Dashport is a dictionary where the key is the keyboard key you want to assign and the action is a dashport action that is defined in the [built-in commands](docs/keyboard_actions.md) of the library. The keys are case-sensitive, so if you want both uppercase and lowercase characters to perform the same action, you'll have to define the key twice.

The `Info` class, which is passed into Dashport's `wrap` function, is for error handling. If curses crashes, it will show a friendly error message along with the dimensions of the terminal, which is usually a contributing factor to the crash.
