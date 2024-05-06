class GUIManager:
    def __init__(self):
        self.labels = {}
        self.entries = {}

    def add_label(self, key, label):
        self.labels[key] = label

    def add_entry(self, key, entry):
        self.entries[key] = entry

    def destroy_label(self, key):
        if key in self.labels:
            self.labels[key].destroy()
            del self.labels[key]

    def destroy_entry(self, key):
        if key in self.entries:
            self.entries[key].destroy()
            del self.entries[key]