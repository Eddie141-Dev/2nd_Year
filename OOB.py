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

class Party:
    def __init__(self, theme, food1, food2, food3, special_food):
        self.theme = theme
        self.food1 = food1
        self.food2 = food2
        self.food3 = food3
        self.special_food = special_food
        self.foods = [food1,food2,food3]

    def __secret_food(self, code):
        if code == "Edward":
            return "Carbonara"
        else:
            return "Not For You!!"

    def list_of_foods(self, code):
        return [self.food1,self.food2,self.food3,self.special_food,self.__secret_food(code)]


Bday_1 = Party("Formal", "Lumpia", "Spaghetti", "Siomai", "Palabok")
print("List:")
print(Bday_1.foods)
print(Bday_1.theme,Bday_1.list_of_foods("Edward"))
Bday_2 = Party("Informal", "Egg", "Sopas", "Hotdog", "Canton")
print("List:")
print(Bday_2.foods)
print(Bday_2.theme,Bday_2.list_of_foods("Ally"))
Bday_3 = Party("Fantasy", "Ambrosia", "Apples of Eden", "Nirvana", "Bread")
print("List:")
print(Bday_3.foods)
print(Bday_3.theme,Bday_3.list_of_foods("Zues"))

# Bday_1 = Party("Formal", "Lumpia", "Spaghetti", "Siomai", "Palabok")
# print(Bday_1.theme,"|", Bday_1.food1,",",Bday_1.food2,",",Bday_1.food3,", |",Bday_1.special_food,"| , |",Bday_1.get_secret_food("Edward"), "|")
# Bday_2 = Party("Informal", "Egg", "Sopas", "Hotdog", "Mac & Cheese")
# print(Bday_2.theme,"|", Bday_2.food1,",",Bday_2.food2,",",Bday_2.food3,", |",Bday_2.special_food,"| , |",Bday_2.get_secret_food("Ally"), "|")
# Bday_1 = Party("Fantasy", "Ambrosia", "Apple of Eden", "Nirvana", "Bread")
# print(Bday_1.theme,"|", Bday_1.food1,",",Bday_1.food2,",",Bday_1.food3,", |",Bday_1.special_food,"| , |",Bday_1.get_secret_food("Xyrus"), "|")