
from dictionaries import Dictionaries
import tkinter as tk
from gui_factory import GUIFactory
from update_components import Update
from calc import Calculations
from components_creation import CreateComp


class Windows:
    def __init__(self, master, utils, gui_manager):
        self.utils = utils
        self.master = master
        self.factory = GUIFactory()
        self.entries = {}
        self.labels = {}
        self.gui_manager = gui_manager
        self.counter_label = None
        self.name_label_row = None
        self.calc = Calculations(self.master)
        self.dictionaries = Dictionaries()
        self.update = Update(self.master, self.gui_manager)
        self.comp = CreateComp(self.master, self.gui_manager)

    def create_window(self):
        pass


class FirstWindow(Windows):
    def create_window(self):
        print("first window method.")
        self.utils.create_label_entry("Name:")

        # Create dropdown entry for Race
        self.utils.create_dropdown_entry(self.master, "Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                                "Half-Orc", "Aasimar"],
                                         command=self.update.update_counter)

        # Create dropdown entries for Class and Level
        self.utils.create_dropdown_entry(self.master, "Class:",
                                         ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian", "Bard",
                                          "Druid", "Monk", "Ranger", "Sorcerer", "Warlock", "Paladin"], command=None)
        self.utils.create_dropdown_entry(self.master, "Level:", [str(i) for i in range(1, 21)],
                                         command=self.update.update_counter)

        # Create dropdown entries for original stats and corresponding modified labels
        for i, stat in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
            # Create entry for original stats
            self.utils.create_dropdown_entry(self.master, stat + ":", [str(i) for i in range(8, 16)],
                                             command=self.update.update_counter)

            # Create label for modified stats
            modified_label = self.factory.create_label(self.master, "Modified " + stat + f": {str(8)}")
            modified_label.grid(row=i + 4, column=2)  # Start from the fourth row, to the right of original stats
            self.utils.gui_manager.labels["Modified " + stat] = modified_label  # Add the label to the labels dictionary

        self.comp.create_next_button()

        self.update.update_counter()


class SecondWindow(Windows):
    def create_window(self):
        for label in self.labels.values():
            label.grid_forget()
        for entry in self.entries.values():
            entry.grid_forget()

        self.utils.hide_next_button()

        # Create new UI elements
        self.utils.create_dropdown_entry(self.master, "Background:",
                                            ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage",
                                             "Soldier"],
                                            command=self.update.update_proficiencies)  # Create background dropdown

        self.comp.create_armor_proficiency_label()

        self.utils.create_dropdown_entry(self.master, "Armour Type:", ["Light", "Medium", "Heavy", "None"],
                                            command=self.update.update_armour_dropdown)
        self.comp.create_hit_points_label()
        self.comp.create_ac_label()  # Recreate counter label

        # Move the armor proficiency label to the appropriate row and column
        if "Armor Proficiency:" in self.labels:
            self.labels["Armor Proficiency:"].grid(row=len(self.labels), column=0, columnspan=2, sticky='w')

        # Move the hit points label to the appropriate row and column
        if "Hit Points:" in self.labels:
            self.labels["Hit Points:"].grid(row=len(self.labels) - 1, column=2, columnspan=2, sticky='w')

        # Keep the counter label
        if self.name_label_row is not None:
            self.counter_label.grid(row=len(self.labels), column=4)

        # Create button to transition to the third window
        self.comp.create_to_third_button()


class ThirdWindow(Windows):
    def create_window(self):
        # Clear the previous window content
        for label in self.labels.values():
            label.grid_forget()
        for entry in self.entries.values():
            entry.grid_forget()

        if "Armour:" in self.labels:
            self.labels["Armour:"].destroy()
            del self.labels["Armour:"]
            del self.entries["Armour:"]

        if "Armor Proficiency:" in self.labels:
            self.labels["Armor Proficiency:"].destroy()
            del self.labels["Armor Proficiency:"]
            del self.entries["Class:"]  # Fix the key here

        self.utils.hide_next_button()
        self.utils.hide_third_window_button()

        # Define the fields for the third window
        fields = [
            "History:", "Hair:", "Skin:", "Eyes:", "Height:", "Weight:", "Age:", "Gender:", "Alignment:"
        ]

        # Create new UI elements for the third window
        for field in fields:
            self.utils.create_label_entry(field)

        self.comp.create_submit_button()