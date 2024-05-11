import tkinter as tk

from character_builder import CharacterBuilder
from events import EventHandler
from windows_management import FirstWindow, SecondWindow, ThirdWindow, FourthWindow
from gui_manager import GUIManager


def main():
    root = tk.Tk()

    # Instantiate GUI-related objects
    gui_manager = GUIManager(root)
    character_builder = CharacterBuilder()

    # Instantiate windows
    fourth_window = FourthWindow(root, gui_manager, character_builder)
    third_window = ThirdWindow(root, gui_manager, fourth_window)
    second_window = SecondWindow(root, gui_manager, third_window)
    first_window = FirstWindow(root, gui_manager, second_window)

    # Instantiate and set up event handler
    event_handler = EventHandler(root, gui_manager)
    event_handler.set_windows(first_window, second_window, third_window, fourth_window)

    # Set up event handler in windows
    first_window.set_event_handler(event_handler)
    second_window.set_event_handler(event_handler)

    # Show first window
    first_window.create_window()

    root.mainloop()

if __name__ == "__main__":
    main()