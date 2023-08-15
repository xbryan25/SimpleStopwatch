import customtkinter as ctk
import buttons

# TODO: Redesign the application


def main():
    app = ctk.CTk()

    app_width = 440
    app_height = 230

    app.geometry(f"{app_width}x{app_height}")
    app.eval("tk::PlaceWindow . center")

    app.resizable(False, False)
    app.title("SimpleStopwatch v1.0 by xbryan")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    buttons.Buttons(app)

    app.mainloop()


if __name__ == '__main__':
    main()
