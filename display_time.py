import customtkinter as ctk
import time


class DisplayTime:
    def __init__(self, window):

        self.window = window

        self.font_tuple = ("Times New Roman", 50)

        self.second = 0
        self.minute = 0
        self.hour = 0

        self.stop = 0

        # Initializing the label
        self.time_label = ctk.CTkLabel(self.window, text="00:00:00", fg_color="transparent",
                                       font=self.font_tuple)
        self.time_label.place(x=120, y=50)

    def start_time(self):

        # The delay is 0.97 seconds to match the delay of the label.after function
        time.sleep(0.97)
        self.second += 1

        if self.second == 60:
            self.second = 0
            self.minute += 1
        elif self.minute == 60:
            self.minute = 0
            self.hour += 1

        if self.stop == 0:
            self.time_label.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
            self.time_label.after(30, lambda: self.start_time())


