import customtkinter as ctk
import buttons


def main():
    app = ctk.CTk()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app.geometry("440x260")
    app.resizable(False, False)
    app.title("SimpleStopwatch by xbryan")

    buttons.Buttons(app)

    app.mainloop()


if __name__ == '__main__':
    main()