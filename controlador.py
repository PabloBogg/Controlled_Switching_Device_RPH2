from tkinter import Tk
from vista import Vista
import customtkinter

# AJUSTES POR DEFECTO
customtkinter.set_appearance_mode("System")  # TEMA
customtkinter.set_default_color_theme("green")  # COLO


class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = Vista(self.root_controler)


if __name__ == "__main__":
    root_tk = customtkinter.CTk()

    Controller(root_tk)

    root_tk.mainloop()
