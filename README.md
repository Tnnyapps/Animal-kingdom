# Animal-kingdom
This is a Python program that contains different animals and their characteristics. The main aim is to teach you  how to contribute to open source projects and the basic github fundamentals you would need in your next job or internship

# How to contribute
To contribute to this project is very easy; this program contains a super class named Animal and
New classes extend this superclass to create different types of animals with different abilities.
To contribute, you can refactor an existing class, add new functionality to a class, or create a new
animal from the pile of animals on [Trellot](URL). The aim of this program is to help you learn the basic fundamentals.
of open source contribution, such as forking a project, registering a PR, or using
project management tools, etc.


# Animal Class Documentation

The `Animal` class is a base class that represents any animal. It has the following attributes:

- `primary_habitat`: a list of strings representing the primary habitats of animals, which include "Air", "Water", and "Land".
- `feeding_behaviour`: a list of strings representing the different feeding behaviors of animals, which include "herbivores", "frugivores", "carnivores", "insectivores", "detritivores", and "omnivores".
- `name`: a string representing the name of the animal.
- `family`: a string representing the family of the animal.
- `endangered`: a boolean value indicating whether the animal is endangered or not.
- `predator`: a list of strings representing the predators of the animal.
- `gestation`: a string representing the length of gestation of the animal.
- `prey`: a list of strings representing the prey of the animal.
- `young`: a string representing the young of the animal.
- `adult_male`: a string representing the name of the adult male of the animal.
- `adult_female`: a string representing the name of the adult female of the animal.
- `sex`: a string representing the sex of the animal.

The `Animal` class has the following methods:

- `__init__(self, sex)`: a constructor that initializes the `sex` attribute of the animal.
- `describe_animal(self)`: a method that prints a description of the animal.
- `eat_animal(self, other)`: a method that eats another animal if it is a prey of the current animal.
- `same_family(self, other)`: a method that checks if two animals are in the same family.
- `set_sex(self, sex)`: a method that sets the `sex` attribute of the animal.
- `detect_other_animal(self, other)`: a method that detects another animal.
- `check_prey(self, prey)`: a method that checks if an animal can eat a certain prey.
- `prong(self, other=None)`: a method that makes the animal run away very fast.

# Lion Class Documentation

The `Lion` class is a subclass of the `Animal` class that represents a lion. It has the following attributes:

- `instance_count`: a class attribute that keeps track of the number of instances of the `Lion` class.
- `name`: a string representing the name of the animal.
- `family`: a string representing the family of the animal.
- `predator`: a list of strings representing the predators of the animal.
- `primary_habitat`: a string representing the primary habitat of the animal.
- `gestation`: a string representing the length of gestation of the animal.
- `prey`: a list of strings representing the prey of the animal.
- `adult_male`: a string representing the name of the adult male of the animal.
- `adult_female`: a string representing the name of the adult female of the animal.

The `Lion` class has the following methods:

- `__init__(self, sex)`: a constructor that initializes the attributes of the `Lion` class.
- `roar(self)`: a method that makes the lion roar.
- `hunt_with(self, other, *others)`: a method that allows the lion to hunt with other lions.
- `mark_territory(self)`: a method that allows the lion to mark its territory.

# Antelope Class Documentation

The `Antelope` class is a subclass of the `Animal` class that represents an antelope. It has the following attributes:

- `instance_count`: a class attribute
