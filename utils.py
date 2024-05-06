from gui_factory import GUIFactory
from components_creation import CreateComp
from data_conservation import DataConservation


class Utils:
    def __init__(self, master, gui_manager):
        self.name_label_row = None
        self.master = master
        self.gui_manager = gui_manager
        self.factory = GUIFactory()
        self.comp = CreateComp(self.master, self.gui_manager)

    def create_label_entry(self, label_text):
        row = len(self.gui_manager.labels)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=0)
        entry = self.factory.create_entry(self.master)
        entry.grid(row=row, column=1)
        self.gui_manager.add_label(label_text, label)  # Store label in GUI manager
        self.gui_manager.add_entry(label_text, entry)  # Store entry in GUI manager
        self.name_label_row = row

    def create_dropdown_entry(self, master, label_text, options, command=None):
        row = len(self.gui_manager.labels)
        label = self.factory.create_label(master, label_text)
        label.grid(row=row, column=0)
        dropdown = self.factory.create_dropdown(master, options, command)
        dropdown.grid(row=row, column=1)
        dropdown.config(anchor='w')
        self.gui_manager.add_label(label_text, label)  # Store label in GUI manager
        self.gui_manager.add_entry(label_text, dropdown)

    def hide_next_button(self):
        if self.comp.next_button:
            self.comp.next_button.grid_forget()

    def hide_third_window_button(self):
        if self.comp.to_third_button:
            self.comp.to_third_button.grid_forget()
