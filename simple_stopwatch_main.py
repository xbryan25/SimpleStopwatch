import customtkinter as ctk
import ctypes as ct

import buttons


def main():
    app = ctk.CTk()

    app_width = 440
    app_height = 230

    app.geometry(f"{app_width}x{app_height}")
    app.eval("tk::PlaceWindow . center")

    myappid = u'mycompany.myproduct.subproduct.version'
    ct.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app.resizable(False, False)
    app.title("SimpleStopwatch v1.0 by xbryan")

    app.iconbitmap("Assets/stopwatch_night.ico")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    buttons.Buttons(app)

    app.mainloop()


if __name__ == '__main__':
    main()
