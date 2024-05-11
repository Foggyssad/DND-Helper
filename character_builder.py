class CharacterBuilder:
    def __init__(self):
        self.name = None
        self.race = None
        self.character_class = None
        self.stats = None
        self.level = None
        self.hit_points = None
        self.skill_proficiencies = None
        self.tool_proficiencies = None
        self.inventory = None
        self.armor_class = None
        self.background = None
        self.history = None
        self.hair = None
        self.skin = None
        self.eyes = None
        self.height = None
        self.weight = None
        self.age = None
        self.gender = None
        self.alignment = None

    def set_level(self, level):
        self.level = level
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_race(self, race):
        self.race = race
        return self

    def set_character_class(self, character_class):
        self.character_class = character_class
        return self

    def set_stats(self, stats):
        self.stats = stats
        return self

    def set_hit_points(self, hit_points):
        self.hit_points = hit_points
        return self

    def set_skill_proficiencies(self, skill_proficiencies):
        self.skill_proficiencies = skill_proficiencies
        return self

    def set_tool_proficiencies(self, tool_proficiencies):
        self.tool_proficiencies = tool_proficiencies
        return self

    def set_inventory(self, inventory):
        self.inventory = inventory
        return self

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class
        return self

    def set_background(self, background):
        self.background = background
        return self

    def set_history(self, history):
        self.history = history
        return self

    def set_hair(self, hair):
        self.hair = hair
        return self

    def set_skin(self, skin):
        self.skin = skin
        return self

    def set_eyes(self, eyes):
        self.eyes = eyes
        return self

    def set_height(self, height):
        self.height = height
        return self

    def set_weight(self, weight):
        self.weight = weight
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_gender(self, gender):
        self.gender = gender
        return self

    def set_alignment(self, alignment):
        self.alignment = alignment
        return self

    def build(self):
        return Character(self.name, self.race, self.character_class, self.stats, self.level, self.hit_points,
                         self.skill_proficiencies, self.tool_proficiencies, self.inventory, self.armor_class,
                         self.background, self.history, self.hair, self.skin, self.eyes, self.height, self.weight,
                         self.age, self.gender, self.alignment)


class Character:
    def __init__(self, name, race, character_class, stats, level, hp, skill_proficiencies, tool_proficiencies,
                 inventory, armour_class, background, history, hair, skin, eyes, height, weight, age, gender,
                 alignment):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.stats = stats
        self.level = level
        self.hp = hp
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.inventory = inventory
        self.armour_class = armour_class
        self.background = background
        self.history = history
        self.hair = hair
        self.skin = skin
        self.eyes = eyes
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.alignment = alignment