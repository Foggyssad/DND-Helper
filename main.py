import tkinter as tk
from gui_factory import GUIFactory
from character_builder_gui import CharacterBuilderGUI


def main():
    root = tk.Tk()
    factory = GUIFactory()
    app = CharacterBuilderGUI(root, factory)
    root.mainloop()


if __name__ == "__main__":
    main()