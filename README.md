# Dungeons and Dragons (DND) Character Sheet Creator

## Introduction:

1. The purpose of the application is to provide the user with an interface to create character sheet for tabletop RPG DND.
2. To start the program download the repository and launch the main.py script; alternatively the application can be started by going to the folder `dist` and running the `main.exe` executable file.
3. The process of using the program is quite straight forward: fill the labels, choose the desired options for character's characteristics and gain access to the character sheet.

## OOP Principles implementation:

1. **Encapsulation**: Encapsulation is demonstrated throughout the code by using classes to encapsulate related functionality and data. The `Calculations` class encapsulates the logic for computing character statistics, abstracts away the details of data access.
2. **Inheritance**: Inheritance is utilized in the logic of creating windows to create relashionships between classes. The classes `FirstWindow`, `SecondWindow`, `ThirdWindow`, `ForthWindow` and `CharactersWindow` classes inherit from the `Window` class, and the GUI creation logic in `GUIFactory` class is biuld on iheritance.
3. **Polymorphism**: Polymorphism is demonstrated through method overriding and method overloading. Subclasses `LabelComponent`, `EntryComponent`, `DropdownComponent`, `ButtonComponent` override the method `create()` from parant class `GUIComponent` to provide specific implementations.
4. **Abstraction**: Abstraction is used to hide the internal implementation details of classes and expose only relevant functionalities. For instance, the `GUIComponent` class provides an abstract method `create()`, leaving the implementation details to its subclasses.

## Body/Analysis: Functional requirements.

### Design Patterns:
1. **Abstarct Factory**: The `GUIFactory` class acts as a concrete implementation of `AstractFactory` class. Each method in `GUIFactory`
 subclass provides a specific implementation for creating GUI components.
```py
class AbstractFactory(ABC):
    @abstractmethod
    def create_label(self, master, text):
        pass

    @abstractmethod
    def create_entry(self, master):
        pass

    @abstractmethod
    def create_dropdown(self, master, options, command):
        pass

    @abstractmethod
    def create_button(self, master, text, command):
        pass


class GUIFactory(AbstractFactory):
    def create_label(self, master, text):
        return LabelComponent().create(master, text=text)

    def create_entry(self, master):
        return EntryComponent().create(master)

    def create_dropdown(self, master, options, command, variable=None):
        return DropdownComponent().create(master, options=options, command=command, variable=variable)

    def create_button(self, master, text, command):
        return ButtonComponent().create(master, text=text, command=command)
```

2. **Builder**: `CharacterBuilder` class is used as a storage for the data entered by user and, once filled, its instance is being passsed around windows. 

```py
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
```

### Reading from File & Writing to File:
The program reads chracacter's characteristics from the instance of CharacterBuilder class and writes them into the JSON file using the `DataConservation` class. The is updated each time the character sheet is updated.

### Testing with unittests:
There are two scripsts for unittests: one checks the functionality of all calculations performed in `Calculations` class and the other one - of `DataConservations` class (filling the CharacterBuilder class' instance and saving data to .json file).
In total there are 6 unittests that cover core functionality.

## Results and Summary

### Results:

1. **Calculations**:
   - Implemented the calculations required for additional character's characteristics based on the fundamental ones
2. **Character Sheet Generation**:
   - Implemented functionalities for generating character sheets with all recorded details, providing a comprehensive overview of the character's traits and abilities.
3. **Character Data Saving And Changing**:
   - Implemented the functionality of changing and saving the data entered by user into a file. 
4. **Windows Creation**:
   - Implemented the creation of all windows, thier GUI elements and instances interaction.
5. **Events Handling**:
   - Implemented event handling functionalities for responding to user interactions, such as button clicks, dropdown selections, and text input changes.

### Conclusions:

   The application successfully implements core functionalities related to character creation and management, providing a tool for DND players to create and modify their characters' characteristics.
   The application follows modular design which allows to easily extend and maintain functionality.
   The application will be extended to allow creation of multiple character sheets and some new not yet implemented parameters such as feats and how the level of character affects the stats. 


### Extensibility:

1. **Multiple Characters**: Introduce new functionality of handling and editing not one but multiple characters.
2. **Creation of new windows**: Creating the new subclass for parant class `Window` for each new window. 
3. **Creation of new GUI elements**: By adding the additional subclass into the `GUIComponent` class and new respective method into `GUIFactory` class, the new element could be added.
4. **Creation of additional characteristics**: Can be done through adding characteristic into CharacterBuilder class.
