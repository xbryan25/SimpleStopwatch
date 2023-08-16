# SimpleStopwatch

## What this app does
- Supports the basic functionalities of a stopwatch, such as start, stop, continue, and reset.
- Can be minimized to a small window.
- Supports light and dark mode; it can be toggled according to preference.

## Limitations as of the latest version
- The application freezes when the stopwatch starts (this is due to time.sleep() of the time module in Python).
- The application won't show up in taskbar when it is minimized (this is due to overrideredirect of customtkinter/tkinter).
- Not 100% accurate stopwatch functionality. SimpleStopwatch might be slightly (± 0.5 seconds) faster or slower when compared to another stopwatch.

## Python modules used in this repo
- customtkinter
- ctypes
- time
