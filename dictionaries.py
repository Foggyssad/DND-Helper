class Dictionaries:
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

    POINT_COSTS = {
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 4,
        13: 5,
        14: 7,
        15: 9
    }