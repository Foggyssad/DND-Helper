from dictionaries import Dictionaries
from gui_factory import GUIFactory
from calc import Calculations
from update_UI import Update


class Window:
    def __init__(self, master, gui_manager, second_window, third_window):
        self.master = master
        self.factory = GUIFactory()
        self.dictionaries = Dictionaries()
        self.gui_manager = gui_manager
        self.calc = Calculations()
        self.second_window = second_window
        self.third_window = third_window
        self.update = Update(master, gui_manager)

    def set_event_handler(self, event_handler):
        self.events = event_handler

    def create_window(self):
        pass

    def create_counter_label(self):
        # Create label for displaying remaining points
        self.counter_label = self.factory.create_label(self.master, "Remaining Points: 27")
        self.counter_label.grid(row=len(self.gui_manager.labels), columnspan=3, sticky="se")  # Adjust row and column
        self.gui_manager.labels["Counter"] = self.counter_label

    def create_armor_proficiency_label(self):
        character_class = self.gui_manager.entries["Class:"].cget("text")

        # Get the armor proficiency for the character class
        armor_proficiency = self.dictionaries.CLASS_ARMOUR_PROFICIENCY.get(character_class, "None")

        # Create label for displaying armor proficiency
        armor_proficiency_label = self.factory.create_label(self.master, f"Armor Proficiency: {armor_proficiency}")
        armor_proficiency_label.grid(row=len(self.gui_manager.labels) + 2, columnspan=2)  # Adjust row and column

    def create_hit_points_label(self):
        # Calculate hit points based on character level and constitution modifier
        hit_points = self.calc.calculate_hit_points(self.gui_manager)

        # Create label for displaying hit points
        hit_points_label = self.factory.create_label(self.master, f"Hit Points: {hit_points}")
        hit_points_label.grid(row=len(self.gui_manager.labels) + 1, column=0, columnspan=2)  # Adjust row and column
        self.gui_manager.labels["Hit Points:"] = hit_points_label

    def create_to_third_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window)

        self.to_third_button = self.factory.create_button(self.master, "Go to Third Window",
                                                          command=self.events.on_to_third_button_click)
        self.to_third_button.grid(row=len(self.gui_manager.labels) + 5, columnspan=3, sticky="se")
        self.gui_manager.buttons["To third"] = self.to_third_button

    def create_ac_label(self):

        # Create label for displaying armor class
        ac_label = self.factory.create_label(self.master, "Armor Class: ")
        ac_label.grid(row=len(self.gui_manager.labels) + 5, column=0)  # Adjust row and column
        self.gui_manager.labels["Armor Class:"] = ac_label

        # Create label for displaying the armor class value (initially set to 10)
        ac_value_label = self.factory.create_label(self.master, "10")
        ac_value_label.grid(row=len(self.gui_manager.labels) + 4, column=1)  # Adjust row and column
        self.gui_manager.labels["Armor Class Value:"] = ac_value_label

    def create_submit_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window)

        self.submit_button = self.factory.create_button(self.master, "Submit character", command=self.events.submit_character)
        self.submit_button.grid(row=len(self.gui_manager.labels) + 2, columnspan=2)  # Adjust row and column
        self.gui_manager.buttons["Submit"] = self.submit_button

    def create_next_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, self.second_window, None)

        self.next_button = self.factory.create_button(self.master, "Next", command=self.events.on_next_button_click)
        self.next_button.grid(row=len(self.gui_manager.labels) + 1, columnspan=3, sticky="se")
        self.gui_manager.labels["Next"] = self.next_button

    def create_armour_dropdown(self):
        self.gui_manager.create_dropdown_entry("Armour Type:", ["Light", "Medium", "Heavy", "None"], command=self.update.update_armour_dropdown)

    def create_background_dropdown(self):
        self.gui_manager.create_dropdown_entry("Background:",
                                   ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage", "Soldier"],
                                   command=self.update.update_proficiencies)


class FirstWindow(Window):
    def __init__(self, master, gui_manager, second_window):
        super().__init__(master, gui_manager, second_window, third_window=None)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        print("first window method.")
        self.gui_manager.create_label_entry("Name:")

        # Create dropdown entry for Race
        self.gui_manager.create_dropdown_entry("Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                                  "Half-Orc", "Aasimar"],
                                            command=self.update.update_counter)

        # Create dropdown entries for Class and Level
        self.gui_manager.create_dropdown_entry("Class:",
                                             ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian", "Bard",
                                              "Druid", "Monk", "Ranger", "Sorcerer", "Warlock", "Paladin"],
                                             command=None)
        self.gui_manager.create_dropdown_entry("Level:", [str(i) for i in range(1, 21)],
                                            command=self.update.update_counter)

        # Create dropdown entries for original stats and corresponding modified labels
        for i, stat in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
            # Create entry for original stats
            self.gui_manager.create_dropdown_entry(stat + ":", [str(i) for i in range(8, 16)],
                                                command=self.update.update_counter)

            # Create label for modified stats
            modified_label = self.factory.create_label(self.master, "Modified " + stat + f": {str(8)}")
            modified_label.grid(row=i + 4, column=2)  # Start from the fourth row, to the right of original stats
            self.gui_manager.labels["Modified " + stat] = modified_label  # Add the label to the labels dictionary

        super().create_next_button()

        self.update.update_counter()


class SecondWindow(Window):
    def __init__(self, master, gui_manager, third_window):
        super().__init__(master, gui_manager, second_window=None, third_window=third_window)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        for key in list(self.gui_manager.labels.keys()):
            self.gui_manager.remove_label(key)
        for key in list(self.gui_manager.entries.keys()):
            self.gui_manager.remove_entry(key)
        for key in list(self.gui_manager.buttons.keys()):
            self.gui_manager.remove_button(key)


        # Create new UI elements
        super().create_background_dropdown()  # Create background dropdown
        super().create_armor_proficiency_label()
        super().create_armour_dropdown()
        super().create_hit_points_label()
        super().create_ac_label()  # Recreate counter label

        # Move the armor proficiency label to the appropriate row and column
        if "Armor Proficiency:" in self.gui_manager.labels:
            self.gui_manager.labels["Armor Proficiency:"].grid(row=len(self.gui_manager.labels), column=0, columnspan=2, sticky='w')

        # Move the hit points label to the appropriate row and column
        if "Hit Points:" in self.gui_manager.labels:
            self.gui_manager.labels["Hit Points:"].grid(row=len(self.gui_manager.labels) - 1, column=2, columnspan=2, sticky='w')

        # Create button to transition to the third window
        super().create_to_third_button()


class ThirdWindow(Window):
    def __init__(self, master, gui_manager):
        super().__init__(master, gui_manager, second_window=None, third_window=None)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        for key in list(self.gui_manager.labels.keys()):
            self.gui_manager.remove_label(key)
        for key in list(self.gui_manager.entries.keys()):
            self.gui_manager.remove_entry(key)
        for key in list(self.gui_manager.buttons.keys()):
            self.gui_manager.remove_button(key)

        # Define the fields for the third window
        fields = [
            "History:", "Hair:", "Skin:", "Eyes:", "Height:", "Weight:", "Age:", "Gender:", "Alignment:"
        ]

        # Create new UI elements for the third window
        for field in fields:
            self.gui_manager.create_label_entry(field)

        super().create_submit_button()
