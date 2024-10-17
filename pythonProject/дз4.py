class Mammal:
    def __init__(self, name):
        self.name = name
        self.has_fur = True

    def feed_young(self):
        print(f"{self.name} feeds its young milk.")

class Canine:
    def bark(self):
        print("Woof!")

class Aquatic:
    def swim(self):
        print("Splash!")

class Animal(Mammal, Canine, Aquatic):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

sea_dog = Animal("Salty", "Sea Dog")
sea_dog.feed_young()
sea_dog.bark()
sea_dog.swim()