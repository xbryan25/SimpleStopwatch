import customtkinter as ctk
import time


class DisplayTime:
    def __init__(self, window):

        self.window = window

        self.font_tuple = ("Times New Roman", 50)

        self.seconds = [0, 0]
        self.minutes = [0, 0]
        self.hours = [0, 0]

        # Initializing the label
        self.time_label = ctk.CTkLabel(self.window, text="00:00:00", fg_color="transparent",
                                       font=self.font_tuple)
        self.time_label.place(x=120, y=50)

    def start_time(self):
        time_start = time.time()
