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

class Favorite_Food:
    def __init__(self, pasta, egg, cheese, pancheta):
        self.pasta = pasta
        self._egg = egg
        self._cheese = cheese
        self.__pancheta = pancheta

    def update_protien(self, protien):
        self.__pancheta = protien

    def new_protien(self):
        return self.__pancheta

    def __str__(self):
        return "This is my Favorite Food!"


Carbonara = Favorite_Food("Rigotoni", "Large Egg", "Parmesano Reggiano", "Bacon")
print(Carbonara)
Carbonara.update_protien("Ham")
print(f"Replacement protien: {Carbonara.new_protien()}")
print("Ingredients:")
print(Carbonara.pasta, "|", Carbonara._egg,"|", Carbonara._cheese,"|", Carbonara.new_protien())
Canton = Favorite_Food("Pancit Canton", "No Egg", "No Cheese", "Pork")
print(Canton)
print("Ingredients:")
print(Canton.pasta, "|", Canton._egg,"|", Canton._cheese,"|", Canton.new_protien())
Rawmen = Favorite_Food("Noodles", "Soft Boiled Egg", "Eden", "Chashu Pork")
print(Rawmen)
print("Ingredients:")
print(Rawmen.pasta, "|", Rawmen._egg,"|", Rawmen._cheese,"|", Rawmen.new_protien())
Sopas = Favorite_Food("Maccaroni", "Soft Boiled Egg", "Mozzarella", "Ham")
print(Sopas)
print("Ingredients:")
print(Sopas.pasta, "|", Sopas._egg,"|", Sopas._cheese,"|", Sopas.new_protien())