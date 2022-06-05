# Boilerplate

Use these examples as starters for your own projects. These examples cover the bare minimum of creating a window, writing text to the screen, and getting used to the concept of the Dashport wrapper and how the program loop works.

## basic_window

### Summary
Creates a basic window with a keyboard command to quit. Also demonstrates creating text on the screen.

### Details

The `Info` class, which is passed into Dashport's `wrap` function, is for error handling. If curses crashes, it will show a friendly error message along with the dimensions of the terminal, which is usually a contributing factor to the crash.
