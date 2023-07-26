import customtkinter as ctk
import time


class Buttons:
    def __init__(self, window):

        self.window = window

        # Initializing the buttons
        self.start_button = ctk.CTkButton(self.window, text="Start",
                                          hover_color='blue', width=100, height=75)
        self.start_button.place(x=35, y=150)

        self.stop_button = ctk.CTkButton(self.window, text="Stop",
                                         hover_color='blue', width=100, height=75)
        self.stop_button.place(x=160, y=150)

        self.reset_button = ctk.CTkButton(self.window, text="Reset",
                                          hover_color='blue', width=100, height=75)
        self.reset_button.place(x=305, y=150)
