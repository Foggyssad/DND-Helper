import unittest
from unittest.mock import MagicMock
from calc import Calculations


class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculations = Calculations()
        self.gui_manager = MagicMock()

    def test_calculate_dexterity_modifier(self):
        # Mocking the GUI Manager entries
        self.gui_manager.entries = {
            "Dexterity:": MagicMock(cget=MagicMock(return_value=12)),
            "Race:": MagicMock(cget=MagicMock(return_value="Elf"))
        }

        dex_modifier = self.calculations.calculate_dexterity_modifier(self.gui_manager)
        self.assertEqual(dex_modifier, 2)  # +1 from race +1 from 12

    def test_calculate_hit_points(self):
        # Mocking the GUI Manager entries
        self.gui_manager.entries = {
            "Class:": MagicMock(cget=MagicMock(return_value="Fighter")),
            "Level:": MagicMock(cget=MagicMock(return_value=3)),
            "Constitution:": MagicMock(cget=MagicMock(return_value=14)),
            "Race:": MagicMock(cget=MagicMock(return_value="Dwarf"))
        }

        hit_points = self.calculations.calculate_hit_points(self.gui_manager)
        self.assertTrue(18 <= hit_points <= 36)  # Assuming hit dice is 10

    def test_calculate_armour_class(self):
        # Mocking the GUI Manager entries
        self.gui_manager.entries = {
            "Armour Type:": MagicMock(cget=MagicMock(return_value="Light")),
            "Armour:": MagicMock(cget=MagicMock(return_value="Leather"))
        }
        self.gui_manager.labels = {"Armor Class Value:": MagicMock(config=MagicMock())}

        # Mocking the dexterity modifier calculation
        self.calculations.calculate_dexterity_modifier = MagicMock(return_value=4)

        armour_class = self.calculations.calculate_armour_class(self.gui_manager)
        self.assertEqual(armour_class, 15)  # Leather armour's AC is 11. + 4 from dexterity modifier

    def test_get_armour_ac(self):
        armour_ac = self.calculations.get_armour_ac("Breastplate")
        self.assertEqual(armour_ac, 14)  # Chainmail AC is 16 in the dictionary

        

if __name__ == '__main__':
    unittest.main()