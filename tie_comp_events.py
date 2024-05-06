from data_conservation import DataConservation


class Tie:
    def __init__(self, second_window, third_window, gui_manager):
        self.gui_manager = gui_manager
        self.data_conservation = DataConservation(self)
        self.second_window = second_window
        self.third_window = third_window

    def on_next_button_click(self):
       self.data_conservation.save_data_first()
       self.second_window.create_window()

    def submit_character(self):
        self.data_conservation.save_data_third()
        self.data_conservation.save_to_file("character_sheet.json")

    def on_to_third_button_click(self):
        self.data_conservation.save_data_second()  # Save entered data
        self.data_conservation.save_to_file("character_sheet.json")  # Save data to a file
        self.third_window.create_window()