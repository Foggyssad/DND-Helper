from character_builder import CharacterBuilder
from components_creation import CreateComp
from data_conservation import DataConservation


class EventHandler:
    def __init__(self, master, first_window, second_window, third_window, gui_manager):
        self.gui_manager = gui_manager
        self.first_window = first_window
        self.second_window = second_window
        self.third_window = third_window
        self.master = master
        self.data_conservation = DataConservation(self.gui_manager)
        self.character_builder = CharacterBuilder()
        self.comp = CreateComp(self.master, self.gui_manager)


    def hide_next_button(self):
        if self.comp.next_button:
            self.comp.next_button.grid_forget()

    def hide_third_window_button(self):
        if self.comp.to_third_button:
            self.comp.to_third_button.grid_forget()

    def on_to_third_button_click(self):
        self.data_conservation.save_data_second()  # Save entered data
        self.data_conservation.save_to_file("character_sheet.json")  # Save data to a file
        self.third_window.create_window()