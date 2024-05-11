from gui_factory import GUIFactory


class GUIManager:
    def __init__(self, master):
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.master = master
        self.factory = GUIFactory()
        self.name_label_row = None

    def create_label_entry(self, label_text, default_text=""):
        row = len(self.labels)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=0)
        entry = self.factory.create_entry(self.master)
        print("Default Text:", default_text)
        print("Entry Widget:", entry)
        entry.insert("end", default_text)  # Use "end" instead of 0 as the index
        entry.grid(row=row, column=1)
        self.add_label(label_text, label)
        self.add_entry(label_text, entry)
        self.name_label_row = row
        return entry

    def create_dropdown_entry(self, label_text, options, command=None):
        row = len(self.labels)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=0)
        dropdown = self.factory.create_dropdown(self.master, options, command)
        dropdown.grid(row=row, column=1)
        dropdown.config(anchor='w')
        self.add_label(label_text, label)
        self.add_entry(label_text, dropdown)
        return dropdown

    def add_label(self, key, label):
        self.labels[key] = label

    def add_entry(self, key, entry):
        self.entries[key] = entry

    def remove_label(self, key):
        if key in self.labels:
            self.labels[key].grid_forget()  # Hide the label instead of destroying it
            # You can optionally keep the label in the dictionary but mark it as hidden
            # self.labels[key].hidden = True

    def remove_entry(self, key):
        if key in self.entries:
            self.entries[key].grid_forget()  # Hide the entry instead of destroying it
            # You can optionally keep the entry in the dictionary but mark it as hidden
            # self.entries[key].hidden = True

    def remove_button(self, key):
        if key in self.buttons:
            self.buttons[key].grid_forget()  # Hide the button instead of destroying it
            # You can optionally keep the button in the dictionary but mark it as hidden
            # self.buttons[key].hidden = True