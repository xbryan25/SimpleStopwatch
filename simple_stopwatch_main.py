import customtkinter as ctk
import buttons

# TODO: Redesign the application
# TODO: Center window upon initialization


def main():
    app = ctk.CTk()
    app.geometry("440x240")
    app.resizable(False, False)
    app.title("SimpleStopwatch by xbryan")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    buttons.Buttons(app)

    app.mainloop()


if __name__ == '__main__':
    main()
