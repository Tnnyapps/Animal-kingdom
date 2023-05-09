"""
To contribute to this project is very easy; this program contains a super class named Animal and
New classes extend this superclass to create different types of animals with different abilities.
To contribute, you can refactor an existing class, add new functionality to a class, or create a new
animal from the pile of animals on Trello. The aim of this program is to help you learn the basic fundamentals.
of open source contribution, such as forking a project, registering a PR, or using
project management tools, etc.
*******************************
Have fun contributing
*****************************
"""


class Animal:
    def __init__(self, sex) -> None:
        self.name = ""
        self.family = ""
        self.endangered = ""
        self.primary_habitat = ["Air", "Water", "Land"]
        self.feeding_behaviour = [
            "herbivores",
            "frugivores",
            "carnivores",
            "insectivores",
            "detritivores",
            "ominivores",
        ]
        self.predator = ""
        self.gestation = 0
        self.prey = []
        self.young = ""
        self.adult_male = ""
        self.adult_female = ""
        self.sex = sex

    def describe_animal(self):
        print(f"This is a {self.name}")

    def eat_animal(self, other):
        if other.name in self.prey:
            print(f"{self.name} gobbles {other.name}")

    def same_family(self, other):
        if self.family == other.family:
            print(f"both {self.name}s are in the same family {self.family}")

    def set_sex(self, sex):
        if sex.lower() == "male":
            self.sex = self.adult_male
        elif sex.lower() == "female":
            self.sex = self.adult_female

    def detect_other_animal(self, other, fn):
        if self.name == other.name:
            print(f"another {self.name} detected")
            return "antelope"
        else:
            print(f"{other.name} detected")
            fn(other)
            return {other.name}

    def check_prey(self, prey):
        if prey.name in self.prey:
            print(f"eats {prey.name}")
        else:
            print("cannot eat prey")
        pass


# Lion class


class Lion(Animal):
    """This class describes a lion as an animal"""

    instance_count = 0

    def __init__(self, sex="male") -> None:
        super().__init__(sex)
        self.name = "lion"
        self.family = "Felidae"
        self.prey = ["antelope", "bufaalo"]
        self.predator = ["cheetah", "lion", "hyena"]
        self.endangered = False
        self.primary_habitat = self.primary_habitat[2]
        self.gestation = "110 days"
        self.adult_male = "lion"
        self.adult_female = "lioness"
        self.young = "cub"
        self.sex = self.sex
        Lion.instance_count += 1
        self.set_sex(sex)

    def roar(self):
        print("lion is roaring!!!")

    def hunt_with(self, other, *others):
        if other.name.lower() == self.name:
            print(f"{Lion.instance_count} lions are now hunting in groups")

    def mark_territory(self):
        print(f"{self.name} is now marking its territory...")


# Antelope
class Antelope(Animal):
    """This class describes an antelope"""

    instance_count = 0

    def __init__(self, sex="male") -> None:
        super().__init__(sex)
        self.name = "antelope"
        self.family = "Antilocapridae"
        self.prey = ["grass", "leaves", "shoots"]
        self.predator = "humans"
        self.endangered = False
        self.primary_habitat = self.primary_habitat[2]
        self.gestation = "260 days"
        self.adult_male = "bull"
        self.adult_female = "cow"
        self.young = "fawn"
        self.sex = sex
        Antelope.instance_count += 1
        self.set_sex(sex)

    def horn_clash(self, other, *others):
        if other.name.lower() == self.name:
            print(f"{Antelope.instance_count} Antelopes are now clashing horns")
        else:
            print(f"cannot clash horns with {other.name}")

    def prong(self):
        print("Antelope is running away veryy fast!")

    def detect_other_animal(self, other, fn=prong):
        super().detect_other_animal(other, fn)


lion1 = Lion("female")
lion2 = Lion("female")
antelope1 = Antelope("female")
antelope2 = Antelope()

antelope1.detect_other_animal(lion1)

