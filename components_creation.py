from dictionaries import Dictionaries
import tkinter as tk
from gui_factory import GUIFactory
from calc import Calculations
from tie_comp_events import Tie


class CreateComp:
    def __init__(self, master, gui_manager):
        self.to_first_button = None
        self.next_button = None
        self.submit_button = None
        self.to_third_button = None
        self.counter_label = None
        self.gui_manager = gui_manager
        self.first_window = None
        self.second_window = None
        self.tie = Tie(self.first_window, self.second_window, self.gui_manager)
        self.master = master
        self.factory = GUIFactory()
        self.entries = {}
        self.labels = {}
        self.calc = Calculations(self.master)
        self.dictionaries = Dictionaries()

    def create_counter_label(self):
        # Create label for displaying remaining points
        self.counter_label = self.factory.create_label(self.master, "Remaining Points: 27")
        self.counter_label.grid(row=len(self.labels), columnspan=3, sticky="se")  # Adjust row and column
        self.labels["Counter"] = self.counter_label

    def create_armor_proficiency_label(self):
        character_class = self.entries["Class:"].cget("text")

        # Get the armor proficiency for the character class
        armor_proficiency = self.dictionaries.CLASS_ARMOUR_PROFICIENCY.get(character_class, "None")

        # Create label for displaying armor proficiency
        armor_proficiency_label = self.factory.create_label(self.master, f"Armor Proficiency: {armor_proficiency}")
        armor_proficiency_label.grid(row=len(self.labels) + 2, columnspan=2)  # Adjust row and column

    def create_hit_points_label(self):
        # Calculate hit points based on character level and constitution modifier
        hit_points = self.calc.calculate_hit_points()

        # Create label for displaying hit points
        hit_points_label = self.factory.create_label(self.master, f"Hit Points: {hit_points}")
        hit_points_label.grid(row=len(self.labels) + 1, column=0, columnspan=2)  # Adjust row and column
        self.labels["Hit Points:"] = hit_points_label

    def create_to_third_button(self):
        self.to_third_button = self.factory.create_button(self.master, "Go to Third Window",
                                                          self.tie.on_to_third_button_click)
        self.to_third_button.grid(row=len(self.labels) + 1, columnspan=2)

    def create_ac_label(self):
        # Create label for displaying armor class
        ac_label = self.factory.create_label(self.master, "Armor Class: ")
        ac_label.grid(row=len(self.labels) + 3, column=0)  # Adjust row and column
        self.labels["Armor Class:"] = ac_label

        # Create label for displaying the armor class value (initially set to 10)
        ac_value_label = self.factory.create_label(self.master, "10")
        ac_value_label.grid(row=len(self.labels) + 3, column=1)  # Adjust row and column
        self.labels["Armor Class Value:"] = ac_value_label

    def create_submit_button(self):
        self.submit_button = self.factory.create_button(self.master, "Submit character", self.tie.submit_character)
        self.submit_button.grid(row=len(self.labels) + 2, columnspan=2)  # Adjust row and column

    def create_next_button(self):
        self.next_button = self.factory.create_button(self.master, "Next", self.tie.on_next_button_click)
        self.next_button.grid(row=len(self.labels) + 1, columnspan=3, sticky="se")
