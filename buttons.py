import customtkinter as ctk
import time
import display_time


class Buttons:
    def __init__(self, window):

        self.window = window

        self.display_time_inst = display_time.DisplayTime(self.window)

        # Initializing the buttons
        self.start_button = ctk.CTkButton(self.window, text="Start",
                                          hover_color='blue', width=100, height=75,
                                          command=lambda: self.start_stopwatch())
        self.start_button.place(x=35, y=150)

        self.stop_button = ctk.CTkButton(self.window, text="Stop",
                                         hover_color='blue', width=100, height=75,
                                         command=lambda: self.stop_stopwatch())
        self.stop_button.place(x=160, y=150)

        self.reset_button = ctk.CTkButton(self.window, text="Reset",
                                          hover_color='blue', width=100, height=75)
        self.reset_button.place(x=305, y=150)

    def start_stopwatch(self):
        self.start_button.configure(state="disabled")

        self.display_time_inst.start_time()

    def stop_stopwatch(self):
        self.display_time_inst.stop_time()

