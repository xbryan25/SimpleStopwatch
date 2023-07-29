import customtkinter as ctk
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

        self.continue_button = ctk.CTkButton(self.window, text="Continue",
                                             hover_color='blue', width=100, height=75,
                                             command=lambda: self.continue_stopwatch())

        self.stop_button = ctk.CTkButton(self.window, text="Stop",
                                         hover_color='blue', width=100, height=75,
                                         command=lambda: self.stop_stopwatch())
        self.stop_button.place(x=160, y=150)
        self.stop_button.configure(state="disabled")

        self.reset_button = ctk.CTkButton(self.window, text="Reset",
                                          hover_color='blue', width=100, height=75,
                                          command=lambda: self.reset_stopwatch())
        self.reset_button.place(x=305, y=150)
        self.reset_button.configure(state="disabled")

    def start_stopwatch(self):
        self.stop_button.configure(state="normal")
        self.start_button.configure(state="disabled")

        if not self.display_time_inst.stop:
            self.display_time_inst.continue_time()
        self.display_time_inst.start_time()

    def stop_stopwatch(self):
        self.display_time_inst.stop_time()

        # Updates button status
        self.reset_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

        # Once stop button is pressed, the continue button will replace it
        if self.start_button.winfo_ismapped():
            self.start_button.place_forget()

        if not self.continue_button.winfo_ismapped():
            self.continue_button.place(x=35, y=150)
        else:
            self.continue_button.configure(state="normal")

    def continue_stopwatch(self):
        # Updates button status
        self.reset_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

        self.display_time_inst.continue_time()
        self.display_time_inst.start_time()

    def reset_stopwatch(self):
        # Updates button status
        self.reset_button.configure(state="disabled")
        self.stop_button.configure(state="disabled")

        self.continue_button.place_forget()

        self.start_button.place(x=35, y=150)
        self.start_button.configure(state="normal")

        self.display_time_inst.stop = False

        self.display_time_inst.reset_time()


