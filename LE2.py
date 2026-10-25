from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, customer):
        self.__customer = customer
        self.__items = []        # List of dicts: {"name": str, "qty": int, "price": float}
        self.__voucher = None    # Stores voucher code string if valid

    # Read-only calculated property for subtotal
    @property
    def subtotal(self):
        total_sub = 0.0
        for item in self.__items:
            total_sub += item["qty"] * item["price"]
        return total_sub

    # Public getters for private attributes needed for formatting
    @property
    def customer(self):
        return self.__customer

    @property
    def items(self):
        return self.__items

    @property
    def voucher(self):
        if self.__voucher is None:
            return "NONE"
        else:
            return self.__voucher

    def add_item(self, item_name, qty, price):
        if qty <= 0:
            return False
        else:
            if price <= 0:
                return False
            else:
                self.__items.append({"name": item_name, "qty": qty, "price": price})
                return True

    def apply_voucher(self, code):
        if code == "SAVE50":
            self.__voucher = code
            return True
        else:
            if code == "SAVE100":
                self.__voucher = code
                return True
            else:
                return False

    def get_voucher_discount(self):
        if self.__voucher == "SAVE50":
            return 50.0
        else:
            if self.__voucher == "SAVE100":
                return 100.0
            else:
                return 0.0

    @abstractmethod
    def compute_total(self):
        pass

    @abstractmethod
    def order_label(self):
        pass


class DineIn(Order):
    def __init__(self, customer, table_no):
        super().__init__(customer)
        self.table_no = table_no

    def order_label(self):
        return f"Dine-In (Table {self.table_no})"

    def compute_total(self):
        sub = self.subtotal
        service_fee = sub * 0.10
        discount = self.get_voucher_discount()
        total = sub + service_fee - discount
        if total < 0:
            return 0.00
        else:
            return round(total, 2)


class Delivery(Order):
    def __init__(self, customer, distance_km):
        super().__init__(customer)
        self.distance_km = distance_km

    def order_label(self):
        return f"Delivery ({self.distance_km}km)"

    def calculate_delivery_fee(self):
        if self.distance_km <= 3:
            return 49.0
        else:
            extra_km = self.distance_km - 3
            return 49.0 + (extra_km * 12.0)

    def compute_total(self):
        sub = self.subtotal
        fee = self.calculate_delivery_fee()
        discount = self.get_voucher_discount()
        total = sub + fee - discount
        if total < 0:
            return 0.00
        else:
            return round(total, 2)


class BulkDelivery(Delivery):
    def __init__(self, customer, distance_km):
        super().__init__(customer, distance_km)

    def order_label(self):
        return f"Bulk Delivery ({self.distance_km}km)"

    def compute_total(self):
        sub = self.subtotal
        fee = self.calculate_delivery_fee()
        discount = self.get_voucher_discount()
        
        # Determine total before checking the bulk discount condition
        temp_total = sub + fee - discount
        if temp_total >= 500:
            fee = 0.0  # Waive the fee
            
        total = sub + fee - discount
        if total < 0:
            return 0.00
        else:
            return round(total, 2)


class Pickup(Order):
    def __init__(self, customer, pickup_minutes):
        super().__init__(customer)
        self.pickup_minutes = pickup_minutes

    def order_label(self):
        return f"Pickup ({self.pickup_minutes} mins)"

    def compute_total(self):
        sub = self.subtotal
        pickup_discount = sub * 0.05
        discount = self.get_voucher_discount()
        total = sub - pickup_discount - discount
        if total < 0:
            return 0.00
        else:
            return round(total, 2)


# --- Application Simulation Execution ---

orders_list = []

# 1. Dine-In Order
order1 = DineIn("Alice Smith", 5)
# Validation for adding item
if order1.add_item("Garlic Parmesan Wings", 2, 180.0):
    print("System: Successfully added item to Order 1.")
else:
    print("System Error: Failed to add item to Order 1 due to invalid constraints.")

# Invalid item validation check
if order1.add_item("Expired Cola", 0, 50.0):
    print("System: Successfully added item to Order 1.")
else:
    print("System Error: Failed to add item to Order 1 due to invalid constraints (Qty/Price is 0).")

# Voucher application check
if order1.apply_voucher("FREEALL"):
    print("System: Voucher FREEALL applied successfully to Order 1.")
else:
    print("System Error: Voucher FREEALL is invalid for Order 1.")

orders_list.append(order1)


# 2. Delivery Order
order2 = Delivery("Bob Jones", 5.5)  # 5.5km -> 49 + (2.5 * 12) = 79PHP fee
order2.add_item("Premium Wagyu Burger", 1, 350.0)
order2.add_item("Truffle Fries", 1, 120.0)
if order2.apply_voucher("SAVE50"):
    print("System: Voucher SAVE50 applied successfully to Order 2.")
else:
    print("System Error: Voucher SAVE50 is invalid for Order 2.")

orders_list.append(order2)


# 3. Pickup Order
order3 = Pickup("Charlie Brown", 15)
order3.add_item("Pepperoni Pizza XL", 1, 450.0)
if order3.apply_voucher("SAVE100"):
    print("System: Voucher SAVE100 applied successfully to Order 3.")
else:
    print("System Error: Voucher SAVE100 is invalid for Order 3.")

orders_list.append(order3)


# 4. Bulk Delivery Order (Total >= 500 requirement check)
order4 = BulkDelivery("Diana Prince", 6)  # 6km -> Delivery fee should be waived if total >= 500
order4.add_item("Family Feast Platter", 1, 550.0)
if order4.apply_voucher("SAVE50"):
    print("System: Voucher SAVE50 applied successfully to Order 4.")
else:
    print("System Error: Voucher SAVE50 is invalid for Order 4.")

orders_list.append(order4)


print("\n" + "="*115)
print(f"{'CUSTOMER':<16} | {'TYPE':<22} | {'ITEMS BOUGHT (QTY)':<30} | {'VOUCHER':<8} | {'SUBTOTAL':<9} | {'FINAL TOTAL':<11}")
print("="*115)

# Formatting loops dynamically call polymorphic functions without isinstance()
for ord_obj in orders_list:
    # Build a clean string list of items bought
    items_summary = ""
    for item in ord_obj.items:
        if items_summary == "":
            items_summary = f"{item['name']} (x{item['qty']})"
        else:
            items_summary += f", {item['name']} (x{item['qty']})"
            
    # Print tabular data using properties and explicit string padding
    print(f"{ord_obj.customer:<16} | {ord_obj.order_label():<22} | {items_summary:<30} | {ord_obj.voucher:<8} | {ord_obj.subtotal:<9.2f} | {ord_obj.compute_total():<11.2f}")

print("="*115)

