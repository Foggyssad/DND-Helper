import json
from character_builder import CharacterBuilder, Character


class DataConservation:
    def __init__(self, gui_manager):
        self.character_builder = CharacterBuilder()
        self.gui_manager = gui_manager

    def save_data(self):
        gui_manager = self.gui_manager
        character_builder = self.character_builder

        # Populate existing CharacterBuilder instance with entered data
        self.set_basic_data(character_builder, gui_manager)
        self.set_additional_data(character_builder, gui_manager)

        self.save_to_file("character_sheet.json")

    def set_basic_data(self, character_builder, gui_manager):
        character_builder.set_name(gui_manager.entries["Name:"].get())
        character_builder.set_race(gui_manager.entries["Race:"].cget("text"))
        character_builder.set_character_class(gui_manager.entries["Class:"].cget("text"))

        modified_stats = {}
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat_value = int(gui_manager.labels["Modified " + stat].cget("text").split(": ")[1])
            modified_stats[stat] = modified_stat_value
        character_builder.set_stats(modified_stats)

        character_builder.set_level(int(gui_manager.entries["Level:"].cget("text")))

    def set_additional_data(self, character_builder, gui_manager):
        character_builder.set_background(gui_manager.entries["Background:"].cget("text"))
        character_builder.set_inventory(gui_manager.entries["Armour:"].cget("text"))
        character_builder.set_armor_class(gui_manager.labels["Armor Class Value:"].cget("text"))
        character_builder.set_skill_proficiencies(gui_manager.labels["Skill Proficiencies:"].cget("text"))
        character_builder.set_tool_proficiencies(gui_manager.labels["Tool Proficiencies:"].cget("text"))
        character_builder.set_hit_points(gui_manager.labels["Hit Points:"].cget("text").replace("Hit Points: ", ""))
        character_builder.set_history(gui_manager.entries["History:"].get())
        character_builder.set_hair(gui_manager.entries["Hair:"].get())
        character_builder.set_skin(gui_manager.entries["Skin:"].get())
        character_builder.set_eyes(gui_manager.entries["Eyes:"].get())
        character_builder.set_height(gui_manager.entries["Height:"].get())
        character_builder.set_weight(gui_manager.entries["Age:"].get())
        character_builder.set_age(gui_manager.entries["Skin:"].get())
        character_builder.set_gender(gui_manager.entries["Gender:"].get())
        character_builder.set_alignment(gui_manager.entries["Alignment:"].get())

    def save_to_file(self, filename):
        # Save updated CharacterBuilder instance to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.character_builder.__dict__, file)