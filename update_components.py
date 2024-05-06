from gui_manager import GUIManager
from utils import Utils
from gui_factory import GUIFactory
import tkinter as tk
from calc import Calculations
from components_creation import CreateComp
from dictionaries import Dictionaries


class Update:
    def __init__(self, master, gui_manager):
        self.remaining_points = 27
        self.master = master
        self.factory = GUIFactory()
        self.gui_manager = gui_manager
        self.utils = Utils(self.master, self.gui_manager)
        self.dictionaries = Dictionaries()
        self.calc = Calculations(self.master)
        self.comp = CreateComp(self.master, self.gui_manager)

    def update_armour_dropdown(self, *args):
        self.utils.gui_manager.destroy_label(["Armour:"])

        # Update the armour dropdown options
        armour_type = self.utils.gui_manager.entries["Armour Type:"].cget("text")
        armours = self.dictionaries.ARMOUR_TYPES.get(armour_type, ["None"])
        self.utils.create_dropdown_entry(self.master, "Armour:", armours, command=self.update_armour_class_value)

        self.calc.calculate_armour_class()

    def update_armour_class_value(self, *args):
        # Calculate the armour class
        character_ac = self.calc.calculate_armour_class()

        # Update the armour class value label
        self.utils.gui_manager.labels["Armor Class Value:"].config(text=str(character_ac))

    def update_counter(self, *args):
        selected_race = self.utils.gui_manager.entries["Race:"].cget("text")
        print(selected_race)
        race_modifiers = self.dictionaries.RACE_STAT_MODIFIERS.get(selected_race,
                                                                   {})  # Get stat modifiers for selected race
        selected_values = [int(self.utils.gui_manager.entries[stat].cget("text")) for stat in
                           ["Strength:", "Dexterity:", "Constitution:",
                            "Intelligence:", "Wisdom:", "Charisma:"]]
        print(selected_values)
        total_cost = 0
        stats_cost = self.dictionaries.POINT_COSTS.copy()
        for value in selected_values:
            total_cost += stats_cost[value]
        self.remaining_points = 27 - total_cost

        # Create the counter label if it doesn't exist
        if "Remaining Points:" not in self.utils.gui_manager.labels:
            self.utils.gui_manager.labels["Remaining Points:"] = self.factory.create_label(self.master, "")
            # Place the counter label in the grid layout
            self.utils.gui_manager.labels["Remaining Points:"].grid(row=len(self.utils.gui_manager.labels), column=0)

        # Update the text of the counter label
        self.utils.gui_manager.labels["Remaining Points:"].config(text=f"Remaining Points: {self.remaining_points}")

        # Update modified stats based on race modifiers
        self.update_modified_labels(selected_values, race_modifiers)

    def update_modified_labels(self, selected_values, race_modifiers):
        # Update modified stats based on race modifiers
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat = selected_values[
                ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"].index(stat)]
            modifier = race_modifiers.get(stat, 0)  # Get the race modifier for the current stat
            modified_stat += modifier
            self.utils.gui_manager.labels["Modified " + stat].config(
                text=f"Modified {stat}: {modified_stat}")  # Update the modified stat label

    def update_proficiencies(self, *args):
        # Remove previous skill and tool proficiency labels if they exist
        for label_key in ["Skill Proficiencies:", "Tool Proficiencies:"]:
            self.utils.gui_manager.destroy_label([f"{label_key}"])

        selected_background = self.utils.gui_manager.entries["Background:"].cget("text")
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
        self.utils.gui_manager.labels["Skill Proficiencies:"] = self.factory.create_label(self.master,
                                                                        "Skill Proficiencies: " + skill_proficiencies)
        self.utils.gui_manager.labels["Skill Proficiencies:"].grid(row=self.utils.name_label_row + 1, column=2, sticky='w')

        self.utils.gui_manager.labels["Tool Proficiencies:"] = self.factory.create_label(self.master,
                                                                       "Tool Proficiencies: " + tool_proficiencies)
        self.utils.gui_manager.labels["Tool Proficiencies:"].grid(row=self.utils.name_label_row + 2, column=2, sticky='w')

    def create_armour_dropdown(self):
        self.utils.create_dropdown_entry(self.master, "Armour Type:", ["Light", "Medium", "Heavy", "None"], command=self.update_armour_dropdown)

    def create_background_dropdown(self):
        self.utils.create_dropdown_entry(self.master, "Background:",
                                   ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage", "Soldier"],
                                   command=self.update_proficiencies)
