# Object Oriented Programing
# Encapsulation (stuff)
# class Lumpia:
#     def __init__(self, main_ingredient, sibuyas, seasoning, gulay):
#         self.main_ingredient = main_ingredient # public
#         self._sibuyas = sibuyas # protected
#         self._seasoning = seasoning # protected
#         self.__gulay = gulay # private

#     def update_gulay(self, new_gulay):
#         self.__gulay = new_gulay

#     def anong_gulay(self):
#         return self.__gulay

#     # def anong_gulay(self, username, password):
#     #     if username == "Edward" and password == "YaoiLover":
#     #         return self.__gulay
#     #     else:
#     #         print("WHO ARE YOU!!!!!!!!")

#     # def __str__(self):
#     #     return "Ang ulam na ito ay Masarap"

# Shanghai = Lumpia("Giniling na Baboy", True, "Magic Sarap", "Carrots")
# Shanghai.update_gulay("Toge")
# print(Shanghai.anong_gulay())
# print(Shanghai.anong_gulay("Ally", "YuriLover"))
# print(Shanghai.anong_gulay("Edward", "YaoiLover"))
# print(Shanghai)

# LA #6

# class Favorite_Food:
#     def __init__(self, pasta, egg, cheese, pancheta):
#         self.pasta = pasta
#         self._egg = egg
#         self._cheese = cheese
#         self.__pancheta = pancheta

#     def update_protien(self, protien):
#         self.__pancheta = protien

#     def new_protien(self):
#         return self.__pancheta

#     def __str__(self):
#         return "This is my Favorite Food!"


# Carbonara = Favorite_Food("Rigotoni", "Large Egg", "Parmesano Reggiano", "Bacon")
# print(Carbonara)
# Carbonara.update_protien("Ham")
# print(f"Replacement protien: {Carbonara.new_protien()}")
# print("Ingredients:")
# print(Carbonara.pasta, "|", Carbonara._egg,"|", Carbonara._cheese,"|", Carbonara.new_protien())
# Canton = Favorite_Food("Pancit Canton", "No Egg", "No Cheese", "Pork")
# print(Canton)
# print("Ingredients:")
# print(Canton.pasta, "|", Canton._egg,"|", Canton._cheese,"|", Canton.new_protien())
# Rawmen = Favorite_Food("Noodles", "Soft Boiled Egg", "Eden", "Chashu Pork")
# print(Rawmen)
# print("Ingredients:")
# print(Rawmen.pasta, "|", Rawmen._egg,"|", Rawmen._cheese,"|", Rawmen.new_protien())
# Sopas = Favorite_Food("Maccaroni", "Soft Boiled Egg", "Mozzarella", "Ham")
# print(Sopas)
# print("Ingredients:")
# print(Sopas.pasta, "|", Sopas._egg,"|", Sopas._cheese,"|", Sopas.new_protien())

# Week 10 & 11

# class Social_media:
#     def __init__(self, username, bday, password):
#         self.username = username
#         self._bday = bday
#         self.__password = password

#     def get_password(self, OTP):
#         if OTP == "Yaoi":
#             return self.__password
#         else:
#             return "Wrong OTP!"
        
#     def __activity_log(self):
#         return ["Visit Ally","Like Xyrus","Post"]

#     def get_activity_log(self, OTP):
#         if OTP == "Yaoi":
#             return ["Visit Ally","Like Xyrus","Post"]
#         else:
#             return "Wrong OTP!"

# Fb = Social_media("Ewdard", "Dec 8, 2007", "YaoiLover")
# print(Fb.get_activity_log("Yaoi"))

# LA #7

# class Party_foods:
#     def __init__(self, theme, special_food):
#         self.theme = theme
#         self.__special_food = special_food

#     def get_secret_food(self, code):
#         if code == "Gin":
#             return self.__special_food
#         else:
#             return "Wrong!"
        
#     def foods(self):
#         return ["Carbonara","Lumpia","Shanghai","Pancit","Palabok","Cake","Ice Cream"]

# Bday1 = Party_foods("Horror","Cordon Bleu")
# print(Bday1.theme,Bday1.get_secret_food("Cordon Bleu"),Bday1.foods())
# Bday2 = Party_foods("Mystical","Gin")
# print(Bday2.theme,Bday2.get_secret_food("Gin"),Bday2.foods())
# Bday3 = Party_foods("Futuristic","Canton")
# print(Bday3.theme,Bday3.get_secret_food("Red Horse"),Bday3.foods())

# class Party:
#     def __init__(self, theme, food1, food2, food3, special_food):
#         self.theme = theme
#         self.food1 = food1
#         self.food2 = food2
#         self.food3 = food3
#         self.special_food = special_food
#         self.foods = [food1,food2,food3]

#     def __secret_food(self, code):
#         if code == "Edward":
#             return "Carbonara"
#         else:
#             return "Not For You!!"

#     def list_of_foods(self, code):
#         return [self.food1,self.food2,self.food3,self.special_food,self.__secret_food(code)]


# Bday_1 = Party("Formal", "Lumpia", "Spaghetti", "Siomai", "Palabok")
# print("List:")
# print(Bday_1.foods)
# print(Bday_1.theme,Bday_1.list_of_foods("Edward"))
# Bday_2 = Party("Informal", "Egg", "Sopas", "Hotdog", "Canton")
# print("List:")
# print(Bday_2.foods)
# print(Bday_2.theme,Bday_2.list_of_foods("Ally"))
# Bday_3 = Party("Fantasy", "Ambrosia", "Apples of Eden", "Nirvana", "Bread")
# print("List:")
# print(Bday_3.foods)
# print(Bday_3.theme,Bday_3.list_of_foods("Zues"))

# Bday_1 = Party("Formal", "Lumpia", "Spaghetti", "Siomai", "Palabok")
# print(Bday_1.theme,"|", Bday_1.food1,",",Bday_1.food2,",",Bday_1.food3,", |",Bday_1.special_food,"| , |",Bday_1.get_secret_food("Edward"), "|")
# Bday_2 = Party("Informal", "Egg", "Sopas", "Hotdog", "Mac & Cheese")
# print(Bday_2.theme,"|", Bday_2.food1,",",Bday_2.food2,",",Bday_2.food3,", |",Bday_2.special_food,"| , |",Bday_2.get_secret_food("Ally"), "|")
# Bday_1 = Party("Fantasy", "Ambrosia", "Apple of Eden", "Nirvana", "Bread")
# print(Bday_1.theme,"|", Bday_1.food1,",",Bday_1.food2,",",Bday_1.food3,", |",Bday_1.special_food,"| , |",Bday_1.get_secret_food("Xyrus"), "|")

# Private Method

# class SocMed:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def __new_password(self, otp, current_passwprd, new_password):

#         if otp == "123" and current_passwprd == self.__password:
#             print("Password Successfully Updated!")

#         else:
#             print("Wrong Credentials! Please Try Agan!")

#     def get_new_password(self, otp, current_passwprd, new_password):
#         self.__new_password(otp, current_passwprd, new_password)

# Fb = SocMed("Edward", "YaoiLover")
# Fb.get_new_password("123","YaoiLover","Siya")

# Decorator

# class Lumpia:
#     def __init__(self, meat, vegtable, seasoning):
#         self.meat = meat
#         self.seasoning = seasoning
#         self.__vegtable = vegtable

#     def wrapper(self, func):
#         def ibalot(*args, **kwargs):
#             print("Preparing...")
#             func(*args, **kwargs)
#             print("Done!")
#         return ibalot

# Shanghai = Lumpia("Beef Giniling", "S & P", "Potatoes & Carrots")
# @Shanghai.wrapper
# def seasoned(spice1, spice2):
#     print(f"Added {spice1} and {spice2} to the filling.")

# @Shanghai.wrapper
# def sautei(ingredient):
#     print(f"Added {ingredient}.")

# seasoned("Paprika", "Turmeric")
# print()
# sautei("Oninon")

# Abstraction

# from abc import ABC, abstractmethod

# class Lumpia(ABC):
#     def __init__(self, meat, vegtable, seasoning):
#         self.meat = meat
#         self.seasoning = seasoning
#         self.__vegtable = vegtable

#     @abstractmethod
#     def add_ingredtient(self, more_sahog):
#         pass

# class Lumpiang_Shanghai(Lumpia):
#     def __init__(self, meat, vegtable, seasoning):
#         self.meat = meat
#         self.seasoning = seasoning
#         self.__vegtable = vegtable
#     def add_ingredtient(self, more_sahog):
#         print(f"The {self.meat}, {self.seasoning}, {self.__vegtable}, and {more_sahog} for the Lumpia, is being cooked")

# Pedro = Lumpiang_Shanghai("beef", "Salt", "Carrots")
# Pedro.add_ingredtient("Onions")

# LA 8

from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def introduce(self):
        print(f"I am {self.name} with {self.hp} HP")

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass

class RangedHero(Hero):
    def __init__(self, name, hp, range):
        super().__init__(name, hp)
        self.range = range

    def attack(self, name, range):
        print(f"I {self.name} attack from {self.range} meters away")

    def ultimate(self):
        return super().ultimate()

class Archer(RangedHero):
    def ultimate(self, ult):
        print(f"I {self.name} cast {ult}!")

class Mage(RangedHero):
    def ultimate(self, ult):
        print(f"I {self.name} proclaim {ult}!")

class MeleeHero(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, name, range):
        print(f"I {self.name} attack, from {range} meters away!")

    def ultimate(self):
        return super().ultimate()

class Warrior(MeleeHero):
    def ultimate(self, ult):
        print(f"I {self.name} attack with {ult}!")

Edward = RangedHero("Edward", 1500, 100)
Edward.introduce()
Edward.attack("Edward", 100)
Edward = Archer("Edward", 1500, 100)
Edward.ultimate("Rain of Sorrow")
print()
Ally = RangedHero("Ally", 1000, 75)
Ally.introduce()
Ally.attack("Ally", 75)
Ally = Mage("Ally", 1000, 75)
Ally.ultimate("Heavenly Smite")
print()
Bear = MeleeHero("Bearned", 10000)
Bear.introduce()
Bear.attack("Bearned", 10)
Bear = Warrior("Bearned", 10000)
Bear.ultimate("Grevious Claw")
print()

list = [Archer("Edward", 1500, 100), Mage("Ally", 1000, 75), Warrior("Bearned", 10000)]
for i in list:
    print(i.attack(Archer, 10))

    
