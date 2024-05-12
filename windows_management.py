from character_builder import CharacterBuilder
from dictionaries import Dictionaries
from gui_factory import GUIFactory
from calc import Calculations
from update_UI import Update


class Window:
    def __init__(self, master, gui_manager, second_window, third_window, fourth_window, character_builder):
        self.master = master
        self.factory = GUIFactory()
        self.dictionaries = Dictionaries()
        self.gui_manager = gui_manager
        self.calc = Calculations()
        self.second_window = second_window
        self.third_window = third_window
        self.fourth_window = fourth_window
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder

    def set_event_handler(self, event_handler):
        self.events = event_handler

    def create_window(self):
        pass

    def clear_window(self):
        for key in list(self.gui_manager.labels.keys()):
            self.gui_manager.remove_label(key)
        for key in list(self.gui_manager.entries.keys()):
            self.gui_manager.remove_entry(key)
        for key in list(self.gui_manager.buttons.keys()):
            self.gui_manager.remove_button(key)

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
        self.gui_manager.labels["Armor Proficiency"] = armor_proficiency_label

    def create_hit_points_label(self):
        # Calculate hit points based on character level and constitution modifier
        hit_points = self.calc.calculate_hit_points(self.gui_manager)

        # Create label for displaying hit points
        self.gui_manager.row_count = 3
        hit_points = self.gui_manager.create_label(f"Hit Points:{hit_points}")
        self.gui_manager.labels["Hit Points:"] = hit_points


    def create_to_third_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window, None, None)

        self.to_third_button = self.factory.create_button(self.master, "Go to Third Window",
                                                          command=self.events.on_to_third_button_click)
        self.to_third_button.grid(row=len(self.gui_manager.labels) + 5, columnspan=3, sticky="se")
        self.gui_manager.buttons["To third"] = self.to_third_button

    def create_ac_label(self):

        # Create label for displaying armor class
        self.gui_manager.row_count = 6
        self.gui_manager.create_label("Armor Class: ")
        self.gui_manager.row_count = 6
        self.gui_manager.column_count = 1
        armour_class = self.gui_manager.create_label("10")
        self.gui_manager.labels["Armor Class Value:"] = armour_class


    def create_submit_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window, self.fourth_window, None)

        self.submit_button = self.factory.create_button(self.master, "Submit character",
                                                        command=self.events.submit_character)
        self.submit_button.grid(row=len(self.gui_manager.labels) + 2, columnspan=2)  # Adjust row and column
        self.gui_manager.buttons["Submit"] = self.submit_button

    def create_next_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, self.second_window, None, None, None)

        self.next_button = self.factory.create_button(self.master, "Next", command=self.events.on_next_button_click)
        self.next_button.grid(row=len(self.gui_manager.labels) + 1, columnspan=3, sticky="se")
        self.gui_manager.labels["Next"] = self.next_button

    def create_armour_dropdown(self):
        self.gui_manager.create_dropdown_entry("Armour Type:", ["Light", "Medium", "Heavy", "None"],
                                               command=self.update.update_armour_dropdown)

    def create_background_dropdown(self):
        self.gui_manager.row_count = 0
        self.gui_manager.create_dropdown_entry("Background:",
                                               ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage",
                                                "Soldier"],
                                               command=self.update.update_proficiencies)

    def create_save_button(self):
        # Example function to create an "Edit" button
        save_button = self.factory.create_button(self.master, "Save", command=self.events.on_save_button_click)
        save_button.grid(row=len(self.gui_manager.labels) + 1, columnspan=2)
        self.gui_manager.buttons["Save"] = save_button


class FirstWindow(Window):
    def __init__(self, master, gui_manager, second_window, character_builder):
        super().__init__(master, gui_manager, second_window, third_window=None, fourth_window=None,
                         character_builder=character_builder)
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
    def __init__(self, master, gui_manager, third_window, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=third_window, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        super().clear_window()

        # Create new UI elements
        super().create_background_dropdown()  # Create background dropdown
        self.update.update_proficiencies()
        super().create_armor_proficiency_label()
        super().create_armour_dropdown()
        super().create_hit_points_label()
        super().create_ac_label()  # Recreate counter label

        # Move the armor proficiency label to the appropriate row and column
        if "Armor Proficiency:" in self.gui_manager.labels:
            self.gui_manager.labels["Armor Proficiency:"].grid(row=len(self.gui_manager.labels), column=0, columnspan=2,
                                                               sticky='w')

        # Move the hit points label to the appropriate row and column
        if "Hit Points:" in self.gui_manager.labels:
            self.gui_manager.labels["Hit Points:"].grid(row=len(self.gui_manager.labels) - 1, column=2, columnspan=2,
                                                        sticky='w')

        # Create button to transition to the third window
        super().create_to_third_button()


class ThirdWindow(Window):
    def __init__(self, master, gui_manager, fourth_window, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=fourth_window,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        super().clear_window()

        # Define the fields for the third window
        fields = [
            "History:", "Hair:", "Skin:", "Eyes:", "Height:", "Weight:", "Age:", "Gender:", "Alignment:"
        ]

        # Create new UI elements for the third window
        for field in fields:
            self.gui_manager.create_label_entry(field)
            print(self.gui_manager.entries[field].cget("text"))

        super().create_submit_button()


class FourthWindow(Window):
    def __init__(self, master, gui_manager, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder  # Assuming you pass the character data as an argument

    def create_window(self):
        super().clear_window()

        # Create labels and entries for base characteristics
        self.gui_manager.reset_row_count()

        characteristics = ["name", "race", "character_class", "hit_points", "inventory", "armor_class", "background", "history", "hair",
                           "skin", "eyes", "height", "weight", "age", "gender", "alignment"]

        print("Creating window with", len(characteristics), "characteristics")

        for characteristic in characteristics:
            label_text = characteristic.replace('_', ' ').capitalize() + ":"
            default_text = getattr(self.character_builder, characteristic, "")

            if characteristic == "background":
                # Call function for background
                self.gui_manager.create_dropdown_entry("Background:", ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage",
                                                "Soldier"], default_value=str(default_text), command=self.update.update_proficiencies)
                self.update.update_proficiencies()
            elif characteristic == "race":
                # Call function for race
                self.gui_manager.create_dropdown_entry("Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                                 "Half-Orc", "Aasimar"], default_value=str(default_text),
                                                       command=self.update.update_counter)
                print(default_text)

            else:
                # Use label entry for other characteristics
                self.gui_manager.create_label_entry(label_text, default_text)

        self.gui_manager.reset_row_count()
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            self.gui_manager.column_count = 2
            modified_stat_value = int(self.gui_manager.labels["Modified " + stat].cget("text").split(": ")[1])
            label = self.gui_manager.create_label(f"Modified {stat}: {modified_stat_value}")
            self.gui_manager.labels[f"Modified {stat}"] = label  # Store the reference to the label widget

        super().create_save_button()


class CharactersWindow(Window):
    def __init__(self, master, gui_manager, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder  # Assuming you pass the character data as an argument

    def create_window(self):
        super().clear_window()
        self.gui_manager.reset_row_count()
        self.gui_manager.create_label("Character 1:")
        name_label = self.gui_manager.create_label("Name:")
        self.gui_manager.labels["Name"] = name_label
        self.gui_manager.column_count = 1
        self.gui_manager.row_count = 1
        self.gui_manager.create_label(self.character_builder.name)
        self.gui_manager.column_count = 0
        self.gui_manager.create_button("Edit Character", command=self.events.on_edit_character_button_click)


