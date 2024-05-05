from gui_factory import GUIFactory
from character_builder import CharacterBuilder, POINT_COSTS
import tkinter as tk
import random
import json


class CharacterBuilderGUI:
    CLASS_ARMOUR_PROFICIENCY = {
        "Fighter": "All armor, shields",
        "Bard": "Light armor",
        "Druid": "Light armor, medium armor, shields",
        "Monk": "None",
        "Ranger": "Light armor. medium armor, shields",
        "Sorcerer": "None",
        "Warlock": "Light armor",
        "Wizard": "None",
        "Rogue": "Light armor",
        "Cleric": "Light armor, medium armor, shields",
        "Barbarian": "Light armor, medium armor, shields",
        "Paladin": "All armor, shields"
        # Add more classes and their armor proficiencies as needed
    }

    CLASS_HIT_DICE = {
        "Fighter": 10,
        "Wizard": 6,
        "Rogue": 8,
        "Cleric": 8,
        "Barbarian": 12,
        "Bard": 8,
        "Druid": 8,
        "Monk": 8,
        "Ranger": 10,
        "Sorcerer": 6,
        "Warlock": 8,
        "Paladin": 10
    }

    RACE_STAT_MODIFIERS = {
        "Aarakocra": {"Dexterity": +2, "Wisdom": +1},
        "Dragonborn": {"Strength": +2, "Charisma": +1},
        "Dwarf": {"Constitution": +2},
        "Elf": {"Dexterity": +2},
        "Genasi": {"Constitution": +2},
        "Half-Orc": {"Strength": +2, "Constitution": +1},
        "Aasimar": {"Dexterity": +2, "Wisdom": +1}
        # Add more races and their stat modifiers as needed
    }

    ARMOUR_TYPES = {
        "Light": ["Padded", "Leather", "Studded Leather"],
        "Medium": ["Hide", "Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"],
        "Heavy": ["Ring Mail", "Chain Mail", "Splint", "Plate"]
    }

    ARMOUR_AC = {
        "Padded": 11,
        "Leather": 11,
        "Studded Leather": 12,
        "Hide": 12,
        "Chain Shirt": 13,
        "Scale Mail": 14,
        "Breastplate": 14,
        "Half Plate": 15,
        "Ring Mail": 14,
        "Chain Mail": 16,
        "Splint": 17,
        "Plate": 18
    }

    def __init__(self, master, factory):
        self.to_first_button = None
        self.submit_button = None
        self.to_first_button = None
        self.to_third_button = None
        self.master = master
        self.master.title("Character Builder")
        self.factory = factory
        self.labels = {}
        self.entries = {}
        self.stats_cost = POINT_COSTS.copy()
        self.remaining_points = 27
        self.name_label_row = None
        self.character_builder = CharacterBuilder()

        self.create_components()
        self.create_counter_label()  # Create counter label
        self.update_counter()
        self.create_next_button()

    def create_components(self):
        self.create_label_entry("Name:")
        self.create_dropdown_entry(self.master, "Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                          "Half-Orc", "Aasimar"],
                                   command=self.update_counter)
        self.create_dropdown_entry(self.master, "Class:", ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian", "Bard",
                                                           "Druid", "Monk", "Ranger", "Sorcerer", "Warlock", "Paladin"],
                                   command=None)
        self.create_dropdown_entry(self.master, "Level:", [str(i) for i in range(1, 21)], command=self.update_counter)
        for i, stat in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
            # Create entry for original stats
            self.create_dropdown_entry(self.master, stat + ":", [str(i) for i in range(8, 16)],
                                       command=self.update_counter)
        # Create modified labels starting from the fourth row
        for i, stat in enumerate(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]):
            # Create label for modified stats
            modified_label = self.factory.create_label(self.master, "Modified " + stat + ":")
            modified_label.grid(row=i + 4, column=2)  # Start from the fourth row, to the right of original stats
            self.labels["Modified " + stat] = modified_label  # Add the label to the labels dictionary

        ac_value_label = self.factory.create_label(self.master, "Armor Class Value:")
        ac_value_label.grid(row=len(self.labels) + 3, column=2)  # Adjust row and column
        self.labels["Armor Class Value:"] = ac_value_label

    def create_hit_points_label(self):
        # Calculate hit points based on character level and constitution modifier
        hit_points = self.calculate_hit_points()

        # Create label for displaying hit points
        hit_points_label = self.factory.create_label(self.master, f"Hit Points: {hit_points}")
        hit_points_label.grid(row=len(self.labels) + 1, column=0, columnspan=2)  # Adjust row and column
        self.labels["Hit Points:"] = hit_points_label

    def create_label_entry(self, label_text):
        row = len(self.labels)
        label = self.factory.create_label(self.master, label_text)
        label.grid(row=row, column=0)
        entry = self.factory.create_entry(self.master)
        entry.grid(row=row, column=1)
        self.labels[label_text] = label
        self.entries[label_text] = entry

        # Add the label to the labels dictionary with row information
        self.name_label_row = row

    def create_dropdown_entry(self, master, label_text, options, command=None):
        row = len(self.labels)
        label = self.factory.create_label(master, label_text)
        label.grid(row=row, column=0)
        dropdown = self.factory.create_dropdown(master, options, command)
        dropdown.grid(row=row, column=1)
        dropdown.config(anchor='w')
        self.labels[label_text] = label
        self.entries[label_text] = dropdown

    def create_counter_label(self):
        # Create label for displaying remaining points
        self.counter_label = self.factory.create_label(self.master, "Remaining Points: 27")
        self.counter_label.grid(row=len(self.labels), columnspan=2)  # Adjust row and column
        self.labels["Counter"] = self.counter_label

    def update_counter(self, *args):
        selected_race = self.entries["Race:"].cget("text")
        race_modifiers = self.RACE_STAT_MODIFIERS.get(selected_race, {})  # Get stat modifiers for selected race
        selected_values = [int(self.entries[stat].cget("text")) for stat in ["Strength:", "Dexterity:", "Constitution:",
                                                                             "Intelligence:", "Wisdom:", "Charisma:"]]
        total_cost = 0
        for value in selected_values:
            total_cost += self.stats_cost[value]
        self.remaining_points = 27 - total_cost

        # Update counter label text
        self.counter_label.config(text=f"Remaining Points: {self.remaining_points}")

        # Update modified stats based on race modifiers
        self.update_modified_labels(selected_values, race_modifiers)

    def update_modified_labels(self, selected_values, race_modifiers):
        # Update modified stats based on race modifiers
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat = selected_values[
                ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"].index(stat)]
            modifier = race_modifiers.get(stat, 0)  # Get the race modifier for the current stat
            modified_stat += modifier
            self.labels["Modified " + stat].config(
                text=f"Modified {stat}: {modified_stat}")  # Update the modified stat label

    def save_data_first(self):
        # Populate existing CharacterBuilder instance with entered data
        self.character_builder.set_name(self.entries["Name:"].get())
        self.character_builder.set_race(self.entries["Race:"].cget("text"))
        self.character_builder.set_character_class(self.entries["Class:"].cget("text"))

        # Pick stats from modified labels
        modified_stats = {}
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat_value = int(self.labels["Modified " + stat].cget("text").split(": ")[1])
            modified_stats[stat] = modified_stat_value
        self.character_builder.set_stats(modified_stats)

        self.character_builder.set_level(int(self.entries["Level:"].cget("text")))

    def save_data_second(self):
        self.character_builder.set_background(self.entries["Background:"].cget("text"))
        self.character_builder.set_inventory(self.entries["Armour:"].cget("text"))
        self.character_builder.set_armor_class(self.calculate_armour_class())
        self.character_builder.set_skill_proficiencies(self.labels["Skill Proficiencies:"].cget("text"))
        self.character_builder.set_tool_proficiencies(self.labels["Tool Proficiencies:"].cget("text"))
        self.character_builder.set_hit_points(self.calculate_hit_points())

    def save_data_third(self):
        self.character_builder.set_history(self.entries["History:"].get())
        self.character_builder.set_hair(self.entries["Hair:"].get())
        self.character_builder.set_skin(self.entries["Skin:"].get())
        self.character_builder.set_eyes(self.entries["Eyes:"].get())
        self.character_builder.set_height(self.entries["Height:"].get())
        self.character_builder.set_weight(self.entries["Age:"].get())
        self.character_builder.set_age(self.entries["Skin:"].get())
        self.character_builder.set_gender(self.entries["Gender:"].get())
        self.character_builder.set_alignment(self.entries["Alignment:"].get())

    def create_second_window(self):
        # Clear the previous window content
        for label in self.labels.values():
            label.grid_forget()
        for entry in self.entries.values():
            entry.grid_forget()

        self.hide_next_button()

        # Create new UI elements
        self.create_background_dropdown()  # Create background dropdown
        self.create_armor_proficiency_label()
        self.create_armour_dropdown()  # Create armour dropdown
        self.create_hit_points_label()
        self.create_ac_label()  # Recreate counter label

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
        self.create_to_third_button()

    def create_to_third_button(self):
        self.to_third_button = self.factory.create_button(self.master, "Go to Third Window",
                                                          self.on_to_third_button_click)
        self.to_third_button.grid(row=len(self.labels) + 1, columnspan=2)  # Adjust row and column

    def on_to_third_button_click(self):
        self.save_data_second()  # Save entered data
        self.save_to_file("character_sheet.json")  # Save data to a file
        self.create_third_window(self.character_builder)

    def save_to_file(self, filename):
        # Save updated CharacterBuilder instance to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.character_builder.__dict__, file)

    def create_ac_label(self):
        # Create label for displaying armor class
        ac_label = self.factory.create_label(self.master, "Armor Class: ")
        ac_label.grid(row=len(self.labels) + 3, column=0)  # Adjust row and column
        self.labels["Armor Class:"] = ac_label

        # Create label for displaying the armor class value (initially set to 10)
        ac_value_label = self.factory.create_label(self.master, "10")
        ac_value_label.grid(row=len(self.labels) + 3, column=1)  # Adjust row and column
        self.labels["Armor Class Value:"] = ac_value_label

    def create_armor_proficiency_label(self):
        # Get the character class
        character_class = self.entries["Class:"].cget("text")

        # Get the armor proficiency for the character class
        armor_proficiency = self.CLASS_ARMOUR_PROFICIENCY.get(character_class, "None")

        # Create label for displaying armor proficiency
        armor_proficiency_label = self.factory.create_label(self.master, f"Armor Proficiency: {armor_proficiency}")
        armor_proficiency_label.grid(row=len(self.labels) + 2, columnspan=2)  # Adjust row and column

    def calculate_hit_points(self):
        character_class = self.entries["Class:"].cget("text")
        hit_dice = self.CLASS_HIT_DICE.get(character_class)
        level = int(self.entries["Level:"].cget("text"))

        # Get base constitution from the entry widget
        base_constitution = int(self.entries["Constitution:"].cget("text"))

        # Retrieve the selected race from the entry widget
        selected_race = self.entries["Race:"].cget("text")

        # Get the race modifiers for constitution
        race_modifiers = self.RACE_STAT_MODIFIERS.get(selected_race, {})
        constitution_modifier_from_race = race_modifiers.get("Constitution", 0)

        # Calculate the modified constitution
        modified_constitution = base_constitution + constitution_modifier_from_race

        # Calculate the constitution modifier
        constitution_modifier = (modified_constitution - 10) // 2

        print("Class:", character_class)
        print("Hit Dice:", hit_dice)
        print("Modified Constitution:", modified_constitution)
        print("Constitution Modifier:", constitution_modifier)
        print("Level:", level)

        # Roll hit points for each level starting from the second level
        hit_points_per_level = []
        for lvl in range(1, level + 1):
            if lvl == 1:
                # Set hit points at first level to max possible roll + con modifier
                roll = hit_dice + constitution_modifier
            else:
                roll = random.randint(1, hit_dice) + constitution_modifier
            print("Level:", lvl, "Roll:", roll)
            hit_points_per_level.append(roll)

        total_hit_points = sum(hit_points_per_level)
        print("Total Hit Points:", total_hit_points)

        return total_hit_points

    def update_proficiencies(self, *args):
        # Remove previous skill and tool proficiency labels if they exist
        for label_key in ["Skill Proficiencies:", "Tool Proficiencies:"]:
            if label_key in self.labels:
                self.labels[label_key].destroy()
                del self.labels[label_key]

        selected_background = self.entries["Background:"].cget("text")
        skill_proficiencies = ""
        tool_proficiencies = ""

        # Define skill and tool proficiencies for each background
        background_proficiencies = {
            "Acolyte": {"Skill Proficiencies": "Insight, Religion", "Tool Proficiencies": "None"},
            "Criminal": {"Skill Proficiencies": "Deception, Stealth", "Tool Proficiencies": "Thieves' Tools"},
            "Folk Hero": {"Skill Proficiencies": "Animal Handling, Survival",
                          "Tool Proficiencies": "One type of artisan's tools, vehicles (land)"},
            "Haunted One": {"Skill Proficiencies": "Choose two from Arcana, Investigation, Religion, and Survival",
                            "Tool Proficiencies": "None"},
            "Noble": {"Skill Proficiencies": "History, Persuasion", "Tool Proficiencies": "One type of gaming set"},
            "Sage": {"Skill Proficiencies": "Arcana, History", "Tool Proficiencies": "None"},
            "Soldier": {"Skill Proficiencies": "Athletics", "Tool Proficiencies": "Vehicle (land)"}
            # Add more backgrounds and their proficiencies as needed
        }

        # Get proficiencies for the selected background
        if selected_background in background_proficiencies:
            skill_proficiencies = background_proficiencies[selected_background]["Skill Proficiencies"]
            tool_proficiencies = background_proficiencies[selected_background]["Tool Proficiencies"]

        # Create labels for skill and tool proficiencies
        self.labels["Skill Proficiencies:"] = self.factory.create_label(self.master,
                                                                        "Skill Proficiencies: " + skill_proficiencies)
        self.labels["Skill Proficiencies:"].grid(row=self.name_label_row + 1, column=2, sticky='w')

        self.labels["Tool Proficiencies:"] = self.factory.create_label(self.master,
                                                                       "Tool Proficiencies: " + tool_proficiencies)
        self.labels["Tool Proficiencies:"].grid(row=self.name_label_row + 2, column=2, sticky='w')

    def create_next_button(self):
        self.next_button = self.factory.create_button(self.master, "Next", self.on_next_button_click)
        self.next_button.grid(row=len(self.labels) + 1, columnspan=2)  # Adjust row and column

    def calculate_armour_class(self):
        armour_type = self.entries["Armour Type:"].cget("text")
        selected_armour = self.entries["Armour:"].cget("text")

        # Get the armor class value from the ARMOUR_AC dictionary based on the selected armor
        armour_ac = self.get_armour_ac(selected_armour)

        dex_modifier = self.calculate_dexterity_modifier()

        if armour_type == "Light":
            armour_class = armour_ac + dex_modifier
        elif armour_type == "Medium":
            armour_class = armour_ac + min(dex_modifier, 2)
        else:  # Heavy armour
            armour_class = armour_ac

        # Update the armor class value label
        self.labels["Armor Class Value:"].config(text=str(armour_class))

        return armour_class

    def calculate_dexterity_modifier(self):
        base_dexterity = int(self.entries["Dexterity:"].cget("text"))
        selected_race = self.entries["Race:"].cget("text")

        race_modifiers = self.RACE_STAT_MODIFIERS.get(selected_race, {})
        dex_modifier_from_race = race_modifiers.get("Dexterity", 0)

        modified_dex = base_dexterity + dex_modifier_from_race

        dex_modifier = (modified_dex - 10) // 2
        return dex_modifier

    def get_armour_ac(self, armour_name):
        return self.ARMOUR_AC.get(armour_name, 10)  # Default AC value if armour is not found

    def create_armour_dropdown(self):
        self.create_dropdown_entry(self.master, "Armour Type:", ["Light", "Medium", "Heavy", "None"], command=self.update_armour_dropdown)

    def create_background_dropdown(self):
        self.create_dropdown_entry(self.master, "Background:",
                                   ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage", "Soldier"],
                                   command=self.update_proficiencies)

    def update_armour_dropdown(self, *args):
        # Remove the existing Armour dropdown, if it exists
        if "Armour:" in self.labels:
            self.labels["Armour:"].destroy()
            del self.labels["Armour:"]
            del self.entries["Armour:"]

        # Update the armour dropdown options
        armour_type = self.entries["Armour Type:"].cget("text")
        armours = self.ARMOUR_TYPES.get(armour_type, ["None"])
        self.create_dropdown_entry(self.master, "Armour:", armours, command=self.update_armour_class_value)

        self.calculate_armour_class()

    def update_armour_class_value(self, *args):
        # Calculate the armour class
        character_ac = self.calculate_armour_class()

        # Update the armour class value label
        self.labels["Armor Class Value:"].config(text=str(character_ac))

    def on_next_button_click(self):
        self.save_data_first()
        self.create_second_window()

    def hide_next_button(self):
        if self.next_button:
            self.next_button.grid_forget()

    def create_third_window(self, character_builder):
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

        self.hide_next_button()
        self.hide_third_window_button()

        # Define the fields for the third window
        fields = [
            "History:", "Hair:", "Skin:", "Eyes:", "Height:", "Weight:", "Age:", "Gender:", "Alignment:"
        ]

        # Create new UI elements for the third window
        for field in fields:
            self.create_label_entry(field)

        # Create button to transition to the first window
        self.create_to_first_button()

        self.submit_button = self.factory.create_button(self.master, "Submit character", self.submit_character)
        self.submit_button.grid(row=len(self.labels) + 2, columnspan=2)  # Adjust row and column

    def submit_character(self):
        self.save_data_third()
        self.save_to_file("character_sheet.json")

    def hide_third_window_button(self):
        if self.to_third_button:
            self.to_third_button.grid_forget()

    def create_to_first_button(self):
        self.to_first_button = self.factory.create_button(self.master, "Go to First Window", self.on_to_first_button_click)
        self.to_first_button.grid(row=len(self.labels) + 1, columnspan=2)  # Adjust row and column

    def on_to_first_button_click(self):
        self.master.destroy()  # Close the current window
        # Re-create the application with a new root window
        root = tk.Tk()
        app = CharacterBuilderGUI(root, GUIFactory())
        root.mainloop()