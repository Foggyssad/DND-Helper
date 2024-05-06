from dictionaries import Dictionaries
import tkinter as tk
import random


class Calculations:
    def __init__(self, master):
        self.master = master
        self.labels = {}
        self.entries = {}
        self.dictionaries = Dictionaries()

    def calculate_dexterity_modifier(self):
        base_dexterity = int(self.entries["Dexterity:"].cget("text"))
        selected_race = self.entries["Race:"].cget("text")

        race_modifiers = self.dictionaries.RACE_STAT_MODIFIERS.get(selected_race, {})
        dex_modifier_from_race = race_modifiers.get("Dexterity", 0)

        modified_dex = base_dexterity + dex_modifier_from_race

        dex_modifier = (modified_dex - 10) // 2
        return dex_modifier

    def calculate_hit_points(self):
        character_class = self.entries["Class:"].cget("text")
        hit_dice = self.dictionaries.CLASS_HIT_DICE.get(character_class)
        level = int(self.entries["Level:"].cget("text"))

        # Get base constitution from the entry widget
        base_constitution = int(self.entries["Constitution:"].cget("text"))

        # Retrieve the selected race from the entry widget
        selected_race = self.entries["Race:"].cget("text")

        # Get the race modifiers for constitution
        race_modifiers = self.dictionaries.RACE_STAT_MODIFIERS.get(selected_race, {})
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

    def get_armour_ac(self, armour_name):
        return self.dictionaries.ARMOUR_AC.get(armour_name, 10)  # Default AC value if armour is not found
