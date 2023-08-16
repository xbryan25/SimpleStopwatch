import customtkinter as ctk
import time


class DisplayTime:
    def __init__(self, window):

        self.window = window

        self.font_tuple_1 = ("Times New Roman", 60)
        self.font_tuple_2 = ("Times New Roman", 30)

        self.second = 0
        self.minute = 0
        self.hour = 0

        self.stop = False
        self.did_start = False

        # Initializing the label

        self.time_label_max = ctk.CTkLabel(self.window, text="00:00:00", fg_color="transparent",
                                           font=self.font_tuple_1)
        self.time_label_max.place(x=110, y=50)

        self.time_label_min = ctk.CTkLabel(self.window, text="00:00:00", fg_color="transparent",
                                           font=self.font_tuple_2)

    def start_time(self):
        if not self.stop:
            if not self.did_start:
                self.did_start = True

            # The delay is 0.96 seconds to match the delay of the label.after function
            time.sleep(0.96)
            self.second += 1

            if self.second == 60:
                self.second = 0
                self.minute += 1

            # This is if not elif so that self.minute turns to 0 as an hour comes
            if self.minute == 60:
                self.minute = 0
                self.hour += 1

            if self.time_label_max.winfo_ismapped():
                self.time_label_max.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
                self.time_label_max.after(30, lambda: self.start_time())
            else:
                self.time_label_min.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
                self.time_label_min.after(30, lambda: self.start_time())

    def stop_time(self):
        self.stop = True

    def continue_time(self):
        self.stop = False

    def reset_time(self):
        self.second = 0
        self.minute = 0
        self.hour = 0

        self.did_start = False

        self.time_label_max.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
        self.time_label_min.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def time_update(self):
        self.time_label_max.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
        self.time_label_min.configure(text=f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
