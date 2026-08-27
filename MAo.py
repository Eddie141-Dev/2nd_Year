    # Inheritance (Sana all)
# class Appliances:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Kitchen_appliances(Appliances): #Any of the Three
#     def __init__(self, name, price, currency):
#         super().__init__(name, price)
#         self.currency = currency
#     def describe(self):
#         print(f"{self.name} {self.price}{self.currency}")
# Microwave = Kitchen_appliances("Hanabishi", 500, "PHP")
# Microwave.describe()
# Air_fryer = Kitchen_appliances("Mitsubishi", 1500, "PHP")
# Air_fryer.describe()

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        print(f"Phone brand: {self.brand} Model number: {self.model}")
class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)


Samsung = Android("Samsung","xo67b12n420qxz")
Huwawei = Android("Huwawei","db69ef32as53op")
Oppo = Android("Oppo","dw9qje67db420q")
Samsung.describePhone()
Huwawei.describePhone()
Oppo.describePhone()

# Week 7
# Polymorphism: Many forms, a method,function,etc that can be used on many different objects
# Class methods often use polymorphism to have the same method name with different purposes
# class Vechile:
#     def __init__(self, brand):
#         self.brand = brand
#     def description(self):
#         print(f"This vheicle is a {self.brand}")
# class Van(Vechile):
#     pass
# class Motorcycle(Vechile):
#     def description(self):
#         print(f"This motorcycle is a {self.brand}")

# Edward = Van("Toyota")
# Andrei = Motorcycle("Yamata")
# Nuella = Van("Tesla")
# Edward.description()
# Andrei.description()


# participants = [Edward, Andrei, Nuella]
# for name in participants:
#     name.description()


# LA 3
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Woof!")
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Meow!")
class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Chirp!")
class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: ...")

def animal_sounds(animal):
    animal.speak()

Animal_dog = Dog("Golden Retiver")
Animal_cat = Cat("Persian")
Animal_bird = Bird("Parrot")
Animal_fish = Fish("Salmon")

animals = [Animal_dog, Animal_cat, Animal_bird, Animal_fish]

for name in animals:
    animal_sounds(name)