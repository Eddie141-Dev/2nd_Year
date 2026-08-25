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