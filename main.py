import tkinter as tk
from gui_factory import GUIFactory
from Controller import Controller


def main():
    root = tk.Tk()
    controller = Controller(root)
    controller.create_first_window()
    root.mainloop()

if __name__ == "__main__":
    main()