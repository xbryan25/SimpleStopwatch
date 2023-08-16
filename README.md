# SimpleStopwatch

## What this app does
- Supports the basic functionalities of a stopwatch, such as start, stop, continue, and reset.
- Can be minimized to a small window.
- Supports light and dark mode; it can be toggled according to preference.

## Limitations as of the latest version
- The application won't show up in taskbar when it is minimized (this is due to overrideredirect of 
customtkinter/tkinter).
- Not 100% accurate stopwatch functionality. SimpleStopwatch might be slightly (± 0.2 seconds) faster or 
slower when compared to another stopwatch. This is noticeable during longer periods of time.

## Python modules used in this repo
- customtkinter
- ctypes
- time

## Problems encountered
- Difficulty in loading digital clock font because of customtkinter's limitations, decided to not use other fonts 
for now.
- Getting the title bar to stay in dark mode, when switching from minimized to maximized version, the title bar 
changes color. (fixed!)
- Application lags when stopwatch is started, because of time.sleep(). (fixed!)
- Changing the icon in the taskbar and getting the icon to stay (and not disappear) when changing from light mode 
to dark mode (and vice versa).

## References that greatly helped in this project
- [Reference 1](https://www.youtube.com/watch?v=s0cpxPSN4k4&pp=ygUYcmVtb3ZlIHRpdGxlIGJhciB0a2ludGVy) (Remove titlebar 
and mouse drag during minimized version)
- [Reference 2](https://www.youtube.com/watch?v=YQbVvgeumwg) (Load stopwatch time effect)
- [Reference 3](https://www.youtube.com/watch?v=l7IMBy4_nhA) (Help solve the issue of application freezing because 
of time.sleep() (from Reference 2). The application now uses after() from customtkinter)
- [Reference 4](https://www.youtube.com/watch?v=4Gi1sKKn_Ts) (Change title bar color for light and dark modes)
- Comment by @M9-SD at Reference 4 (at end of title bar) ("window.withdraw()" and ("window.deiconify()")
- [Reference 5](https://www.youtube.com/watch?v=Z8jdlBNIaDo) (Center tkinter window on the screen)
- [Reference 6](https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105)
(Set icon in taskbar)
- Comment by Alex Zeleznyak at Reference 6 (add time.sleep() to stop icon from blinking
and disappearing)
