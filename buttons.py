import customtkinter as ctk
import display_time
import ctypes as ct


class Buttons:
    def __init__(self, window):

        self.window = window

        self.display_time_inst = display_time.DisplayTime(self.window)

        # Initializing the buttons

        # When window is maximized
        self.start_button = ctk.CTkButton(self.window, text="Start", font=("Times New Roman", 23),
                                          hover_color='blue', width=100, height=75,
                                          command=lambda: self.start_stopwatch())
        self.start_button.place(x=35, y=150)

        self.continue_button = ctk.CTkButton(self.window, text="Continue", font=("Times New Roman", 23),
                                             hover_color='blue', width=100, height=75,
                                             command=lambda: self.continue_stopwatch())

        self.stop_button = ctk.CTkButton(self.window, text="Stop", font=("Times New Roman", 23),
                                         hover_color='blue', width=100, height=75,
                                         command=lambda: self.stop_stopwatch())
        self.stop_button.place(x=160, y=150)
        self.stop_button.configure(state="disabled")

        self.reset_button = ctk.CTkButton(self.window, text="Reset", font=("Times New Roman", 23),
                                          hover_color='blue', width=100, height=75,
                                          command=lambda: self.reset_stopwatch())
        self.reset_button.place(x=305, y=150)
        self.reset_button.configure(state="disabled")

        self.minimize_button = ctk.CTkButton(self.window, text="-",
                                             hover_color='blue', width=20, height=20,
                                             command=lambda: self.minimize())
        self.minimize_button.place(x=420, y=0)

        # When window is minimized
        self.maximize_button = ctk.CTkButton(self.window, text="+",
                                             hover_color='blue', width=20, height=20,
                                             command=lambda: self.maximize())

        self.exit_button = ctk.CTkButton(self.window, text="x",
                                         hover_color='blue', width=20, height=20,
                                         command=lambda: self.exit())

        self.mini_start_button = ctk.CTkButton(self.window, text="▶",
                                               hover_color='blue', width=20, height=20,
                                               command=lambda: self.start_stopwatch())

        self.mini_continue_button = ctk.CTkButton(self.window, text="▶",
                                                  hover_color='blue', width=20, height=20,
                                                  command=lambda: self.continue_stopwatch())

        self.mini_stop_button = ctk.CTkButton(self.window, text="◼",
                                              hover_color='blue', width=20, height=20,
                                              command=lambda: self.stop_stopwatch())

        self.mini_stop_button.configure(state="disabled")

        self.mini_reset_button = ctk.CTkButton(self.window, text="🔁",
                                               hover_color='blue', width=20, height=20,
                                               command=lambda: self.reset_stopwatch())

        self.mini_reset_button.configure(state="disabled")

    def start_stopwatch(self):
        if self.mini_start_button.winfo_ismapped():
            self.mini_start_button.configure(state="disabled")
            self.mini_start_button.place_forget()

            self.mini_stop_button.configure(state="normal")
            self.mini_stop_button.place(x=0, y=50)

            if not self.display_time_inst.stop:
                self.display_time_inst.continue_time()
            self.display_time_inst.start_time()
        else:
            self.stop_button.configure(state="normal")
            self.start_button.configure(state="disabled")

            if not self.display_time_inst.stop:
                self.display_time_inst.continue_time()
            self.display_time_inst.start_time()

    def stop_stopwatch(self):
        self.display_time_inst.stop_time()

        if self.mini_stop_button.winfo_ismapped():
            self.mini_stop_button.configure(state="disabled")
            self.mini_stop_button.place_forget()

            self.mini_continue_button.configure(state="normal")
            self.mini_continue_button.place(x=0, y=50)

            self.mini_reset_button.configure(state="normal")
        else:
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
        if self.mini_continue_button.winfo_ismapped():
            self.mini_reset_button.configure(state="disabled")

            self.mini_stop_button.configure(state="normal")
            self.mini_stop_button.place(x=0, y=50)

            self.display_time_inst.continue_time()
            self.display_time_inst.start_time()
        else:
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

    def minimize(self):
        self.start_button.place_forget()
        self.continue_button.place_forget()
        self.reset_button.place_forget()
        self.stop_button.place_forget()
        self.minimize_button.place_forget()

        self.display_time_inst.time_label_max.place_forget()
        self.display_time_inst.time_label_min.place(x=35, y=15)

        self.display_time_inst.time_update()

        self.maximize_button.place(x=0, y=0)
        self.exit_button.place(x=155, y=0)

        # Add minimized buttons
        if not self.display_time_inst.did_start:
            self.mini_start_button.place(x=0, y=50)
        else:
            self.mini_continue_button.place(x=0, y=50)

        self.mini_reset_button.place(x=30, y=50)

        # Removes title bar
        self.window.overrideredirect(True)

        self.window.bind("<B1-Motion>", self.move_app)

        self.window.wm_attributes('-topmost', 'True')

        self.window.geometry("175x75")

    def move_app(self, event):
        self.window.geometry(f"+{event.x_root - 110}+{event.y_root - 38}")

    def maximize(self):
        self.window.geometry("440x260")

        self.window.overrideredirect(False)

        self.dark_title_bar()

        self.maximize_button.place_forget()
        self.mini_start_button.place_forget()
        self.mini_stop_button.place_forget()
        self.mini_reset_button.place_forget()
        self.mini_continue_button.place_forget()
        self.exit_button.place_forget()
        self.display_time_inst.time_label_min.place_forget()

        # Add minimized buttons
        if not self.display_time_inst.did_start:
            self.start_button.place(x=35, y=150)
        else:
            self.continue_button.place(x=35, y=150)

        self.stop_button.place(x=160, y=150)
        self.reset_button.place(x=305, y=150)
        self.minimize_button.place(x=420, y=0)

        self.display_time_inst.time_label_max.place(x=120, y=50)
        self.display_time_inst.time_update()

    def dark_title_bar(self):

        # From @Unnmanedbuthere_ from Youtube (for dark title bar) ----------
        self.window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.window.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
        self.window.withdraw()
        self.window.deiconify()
        # ----------------------------------------------------------------

    def exit(self):
        self.window.destroy()
