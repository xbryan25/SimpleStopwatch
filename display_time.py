import customtkinter as ctk
import time
import pyglet

# pyglet is imported to make the font readable to customtkinter
pyglet.font.add_file('/Assets/Fonts/digital-7.ttf')

class DisplayTime:
    def __init__(self, window):

        self.window = window

        self.text = "00:00:00:00"

        # Initializing the buttons
        self.time_label = ctk.CTkLabel(self.window, text=f"{self.text}", fg_color="transparent",
                                       font=("/Assets/Fonts/digital-7.ttf", 25))
        self.time_label.place(x=10, y=50)
