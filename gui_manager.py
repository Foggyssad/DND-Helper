from gui_factory import GUIFactory
import tkinter as tk


class GUIManager:
    def __init__(self, master):
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.master = master
        self.factory = GUIFactory()
        self.name_label_row = None
        self.row_count = 0
        self.column_count = 0

    def reset_row_count(self):
        self.row_count = 0
        self.column_count = 0

    def create_label_entry(self, label_text, default_text=""):
        row = self.row_count
        column = self.column_count
        print("Creating label at row", row, "with text:", label_text)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=column, sticky='w')
        entry = self.factory.create_entry(self.master)
        entry.insert("end", default_text)
        entry.grid(row=row, column=column + 1, padx=5)
        print("Creating entry at row", row, "with default text:", default_text)
        self.row_count += 1
        self.add_label(label_text, label)
        self.add_entry(label_text, entry)
        self.name_label_row = row
        return entry

    def create_label(self, label_text):
        row = self.row_count
        column = self.column_count
        print("Creating label at row", row, "and column", column, "with text:", label_text)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=column, sticky='w')
        self.row_count += 1
        self.add_label(label_text, label)
        return label

    def create_dropdown_entry(self, label_text, options, default_value=None, command=None):
        row = self.row_count
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=0)

        # Create a variable to store the selected value
        selected_value = tk.StringVar(self.master)

        if default_value is None or default_value not in options:
            default_value = options[0]

        selected_value.set(default_value)

        dropdown = self.factory.create_dropdown(self.master, options, command, variable=selected_value)
        dropdown.grid(row=row, column=1)
        self.row_count += 1
        dropdown.config(anchor='w')
        self.add_label(label_text, label)
        self.add_entry(label_text, dropdown)

        return dropdown

    def create_button(self, button_text, command=None):
        row = self.row_count
        column = self.column_count
        print("Creating button at row", row, "and column", column, "with text:", button_text)
        button = self.factory.create_button(self.master, button_text, command)
        button.grid(row=row, column=column)
        self.row_count += 1
        self.add_button(button_text, button)
        return button

    def add_label(self, key, label):
        self.labels[key] = label

    def add_entry(self, key, entry):
        self.entries[key] = entry

    def add_button(self, key, button):
        self.buttons[key] = button

    def remove_label(self, key):
        if key in self.labels:
            self.labels[key].grid_forget()

    def remove_entry(self, key):
        if key in self.entries:
            self.entries[key].grid_forget()

    def remove_button(self, key):
        if key in self.buttons:
            self.buttons[key].grid_forget()