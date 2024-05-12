import unittest
import os
import json
from unittest.mock import MagicMock
from data_conservation import DataConservation


class TestDataConservation(unittest.TestCase):

    def setUp(self):
        self.gui_manager = MagicMock()
        self.data_conservation = DataConservation(self.gui_manager)

        # Mocking GUI Manager entries and labels
        self.gui_manager.entries = {
            "Name:": MagicMock(get=MagicMock(return_value="John")),
            "Race:": MagicMock(cget=MagicMock(return_value="Dwarf")),
            "Class:": MagicMock(cget=MagicMock(return_value="Fighter")),
            "Level:": MagicMock(cget=MagicMock(return_value="1")),
            "Background:": MagicMock(cget=MagicMock(return_value="Noble")),
            "Armour:": MagicMock(cget=MagicMock(return_value="Plate")),
            "History:": MagicMock(get=MagicMock(return_value="A hero's tale")),
            "Hair:": MagicMock(get=MagicMock(return_value="Black")),
            "Skin:": MagicMock(get=MagicMock(return_value="Fair")),
            "Eyes:": MagicMock(get=MagicMock(return_value="Blue")),
            "Height:": MagicMock(get=MagicMock(return_value="6'0\"")),
            "Age:": MagicMock(get=MagicMock(return_value="30")),
            "Gender:": MagicMock(get=MagicMock(return_value="Male")),
            "Alignment:": MagicMock(get=MagicMock(return_value="Lawful Good"))
        }
        self.gui_manager.labels = {
            "Modified Strength": MagicMock(cget=MagicMock(return_value="Modified Strength: 12")),
            "Modified Dexterity": MagicMock(cget=MagicMock(return_value="Modified Dexterity: 10")),
            "Modified Constitution": MagicMock(cget=MagicMock(return_value="Modified Constitution: 14")),
            "Modified Intelligence": MagicMock(cget=MagicMock(return_value="Modified Intelligence: 8")),
            "Modified Wisdom": MagicMock(cget=MagicMock(return_value="Modified Wisdom: 11")),
            "Modified Charisma": MagicMock(cget=MagicMock(return_value="Modified Charisma: 9")),
            "Armor Class Value:": MagicMock(cget=MagicMock(return_value="15")),
            "Skill Proficiencies:": MagicMock(cget=MagicMock(return_value="Acrobatics, Athletics")),
            "Tool Proficiencies:": MagicMock(cget=MagicMock(return_value="Smith's tools")),
            "Hit Points:": MagicMock(cget=MagicMock(return_value="10"))
        }

    def tearDown(self):
        # Remove the test JSON file if it exists
        if os.path.exists("test_character_sheet.json"):
            os.remove("test_character_sheet.json")

    def test_save_data(self):
        # Save the data
        self.data_conservation.save_data()

        # Check if the file exists
        self.assertTrue(os.path.exists("character_sheet.json"))

        # Load the saved data from the file
        with open("character_sheet.json", "r") as file:
            saved_data = json.load(file)

        # Check if the saved data matches the expected data
        expected_data = {
            "name": "John",
            "race": "Dwarf",
            "character_class": "Fighter",
            "stats": {
                "Strength": 12,
                "Dexterity": 10,
                "Constitution": 14,
                "Intelligence": 8,
                "Wisdom": 11,
                "Charisma": 9
            },
            "level": 1,
            "hit_points": "10",
            "skill_proficiencies": "Acrobatics, Athletics",
            "tool_proficiencies": "Smith's tools",
            "inventory": "Plate",
            "armor_class": "15",
            "background": "Noble",
            "history": "A hero's tale",
            "hair": "Black",
            "skin": "Fair",
            "eyes": "Blue",
            "height": "6'0\"",
            "weight": "30",
            "age": "Fair",
            "gender": "Male",
            "alignment": "Lawful Good"
        }

        self.assertDictEqual(saved_data, expected_data)

    def test_data_presence_after_save(self):
        # Save the data
        self.data_conservation.save_data()

        # Load the saved data from the file
        with open("character_sheet.json", "r") as file:
            saved_data = json.load(file)

        # Check if the saved data exists in the CharacterBuilder instance
        character_builder = self.data_conservation.character_builder
        self.assertEqual(character_builder.name, saved_data["name"])
        self.assertEqual(character_builder.race, saved_data["race"])
        self.assertEqual(character_builder.character_class, saved_data["character_class"])
        self.assertEqual(character_builder.stats, saved_data["stats"])
        self.assertEqual(character_builder.level, saved_data["level"])
        self.assertEqual(character_builder.hit_points, saved_data["hit_points"])
        self.assertEqual(character_builder.skill_proficiencies, saved_data["skill_proficiencies"])
        self.assertEqual(character_builder.tool_proficiencies, saved_data["tool_proficiencies"])
        self.assertEqual(character_builder.inventory, saved_data["inventory"])
        self.assertEqual(character_builder.armor_class, saved_data["armor_class"])
        self.assertEqual(character_builder.background, saved_data["background"])
        self.assertEqual(character_builder.history, saved_data["history"])
        self.assertEqual(character_builder.hair, saved_data["hair"])
        self.assertEqual(character_builder.skin, saved_data["skin"])
        self.assertEqual(character_builder.eyes, saved_data["eyes"])
        self.assertEqual(character_builder.height, saved_data["height"])
        self.assertEqual(character_builder.weight, saved_data["weight"])
        self.assertEqual(character_builder.age, saved_data["age"])
        self.assertEqual(character_builder.gender, saved_data["gender"])
        self.assertEqual(character_builder.alignment, saved_data["alignment"])

if __name__ == '__main__':
    unittest.main()
