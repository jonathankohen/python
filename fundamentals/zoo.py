class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}.")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self


class Lion(Animal):
    def __init__(self, name, age, roar="'<small>meow</small>' -Simba", health=20, happiness=20):
        super().__init__(name, age, health, happiness)
        self.roar = roar

    def feed(self):
        self.health += 20
        self.happiness += 20
        return self

    def intimidate(self):
        print(self.roar)
        return self


class Tiger(Animal):
    def __init__(self, name, age, health=20, happiness=5):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 5
        self.happiness += 5
        return self


class Goldfish(Animal):
    def __init__(self, name, age, health=20, happiness=5):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 50
        self.happiness += 50
        return self


# new_animal1 = Animal('Mufasa', 62, 10, 10).display_info()
# new_lion1 = Lion('Simba', 13).display_info()
# new_tiger1 = Tiger("Tabby", 35).display_info()
# new_goldfish1 = Goldfish("Friend", 1).display_info()


class Zoo(Lion):
    def __init__(self, zoo_name):
        self.name = zoo_name


zoo1 = Zoo("John's Zoo")
new_lion1 = Lion('Simba', 13).display_info()
new_lion2 = Lion('Nala', 10).display_info()
new_tiger1 = Tiger("Tabby", 35).display_info()
new_tiger2 = Tiger("Lily", 40).display_info()
