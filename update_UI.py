from gui_factory import GUIFactory
from calc import Calculations
from dictionaries import Dictionaries


class Update:
    def __init__(self, master, gui_manager):
        self.remaining_points = 27
        self.master = master
        self.factory = GUIFactory()
        self.dictionaries = Dictionaries()
        self.calc = Calculations()
        self.gui_manager = gui_manager

    def update_armour_dropdown(self, *args):
        self.gui_manager.remove_label("Armour:")
        self.gui_manager.remove_entry("Armour:")

        # Update the armour dropdown options
        armour_type = self.gui_manager.entries["Armour Type:"].cget("text")
        armours = self.dictionaries.ARMOUR_TYPES.get(armour_type, ["None"])
        self.gui_manager.row_count = 2
        self.gui_manager.create_dropdown_entry("Armour:", armours, command=self.update_armour_class_value)

        self.calc.calculate_armour_class(self.gui_manager)

    def update_armour_class_value(self, *args):
        # Calculate the armour class
        character_ac = self.calc.calculate_armour_class(self.gui_manager)

        # Update the armour class value label
        self.gui_manager.labels["Armor Class Value:"].config(text=str(character_ac))

    def update_counter(self, *args):
        selected_race = self.gui_manager.entries["Race:"].cget("text")
        print(selected_race)
        race_modifiers = self.dictionaries.RACE_STAT_MODIFIERS.get(selected_race,
                                                                   {})  # Get stat modifiers for selected race
        selected_values = [int(self.gui_manager.entries[stat].cget("text")) for stat in
                           ["Strength:", "Dexterity:", "Constitution:",
                            "Intelligence:", "Wisdom:", "Charisma:"]]
        print(selected_values)
        total_cost = 0
        stats_cost = self.dictionaries.POINT_COSTS.copy()
        for value in selected_values:
            total_cost += stats_cost[value]
        self.remaining_points = 27 - total_cost

        # Create the counter label if it doesn't exist
        if "Remaining Points:" not in self.gui_manager.labels:
            self.gui_manager.labels["Remaining Points:"] = self.factory.create_label(self.master, "")
            # Place the counter label in the grid layout
            self.gui_manager.labels["Remaining Points:"].grid(row=len(self.gui_manager.labels), column=0)

        # Update the text of the counter label
        self.gui_manager.labels["Remaining Points:"].config(text=f"Remaining Points: {self.remaining_points}")

        # Update modified stats based on race modifiers
        self.update_modified_labels(selected_values, race_modifiers)

    def update_modified_labels(self, selected_values, race_modifiers):
        # Update modified stats based on race modifiers
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat = selected_values[
                ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"].index(stat)]
            modifier = race_modifiers.get(stat, 0)  # Get the race modifier for the current stat
            modified_stat += modifier

            # Update the modified stat label
            label_key = "Modified " + stat
            label = self.gui_manager.labels[label_key]  # Retrieve the reference to the label widget
            label.config(text=f"Modified {stat}: {modified_stat}")  # Update the GUI label text

    def update_proficiencies(self, *args):
        # Remove previous skill and tool proficiency labels if they exist
        for label_key in ["Skill Proficiencies:", "Tool Proficiencies:"]:
            self.gui_manager.remove_label(f"{label_key}")

        selected_background = self.gui_manager.entries["Background:"].cget("text")
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
        self.gui_manager.labels["Skill Proficiencies:"] = self.factory.create_label(self.master,
                                                                        "Skill Proficiencies: " + skill_proficiencies)
        self.gui_manager.labels["Skill Proficiencies:"].grid(row=self.gui_manager.name_label_row + 1, column=2, sticky='w')

        self.gui_manager.labels["Tool Proficiencies:"] = self.factory.create_label(self.master,
                                                                       "Tool Proficiencies: " + tool_proficiencies)
        self.gui_manager.labels["Tool Proficiencies:"].grid(row=self.gui_manager.name_label_row + 2, column=2, sticky='w')
