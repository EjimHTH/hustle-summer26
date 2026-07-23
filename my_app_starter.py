# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: ___Edgar_______________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: ____Perfume + Skin Care_(Beauty Products)____________________________________
# ============================================================
# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class BeautyProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be below $0.")
        else:
            self.price = amount
            print("Price updated!")
# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
    def deliver(self):
        print(f"Your skincare product '{self.name}' is on the way!")

class Perfume(BeautyProduct):
    def deliver(self):
        print(f"Your perfume '{self.name}' has been carefully packaged and shipped!")    

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
class Perfume(BeautyProduct):
    pass

# TICKET 2: Create real beauty products

item1 = BeautyProduct("Rhode Glazing Milk", 30)
item2 = Perfume("YSL Libre Eau de Parfum", 145)
item3 = BeautyProduct("Laneige Lip Sleeping Mask", 24)

print(item1.name)
print(item2.name)
print(item3.name)

# Prediction:
# I predict this will print: Price cannot be below $0.

# Try to break it
item1.set_price(-5)

# Output:
# Price cannot be below $0.

# Test the deliver() methods
item1.deliver()
item2.deliver()

# EXPLAIN:
# The method is named deliver() in both classes, but each class has its own version.

# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
# TICKET 6: Your cart
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.

    def checkout(self):
        total = 0

        print("\n----- Checkout -----")

        for item in self.items:
            item.deliver()      # Runs the correct deliver() method
            total += item.price

        print("--------------------")
        print("Total: $" + str(total))


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {
    "1": item1,
    "2": item2,
    "3": item3
}
cart = Cart()

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
print("Welcome to Edgar's Beauty Store!")

choice = ""

while choice != "done":
    choice = input("Choose an item (1-3) or type 'done': ")

    if choice == "done":
        print("Finished shopping!")
    elif choice in store:
        cart.add(store[choice])
        print(store[choice].name, "added to your cart!")
    else:
        print("Invalid choice. Please try again.")
#   PREDICT what happens when you pick 1: _____Rhode Glazing Milk added to your cart!_________
cart.checkout()
# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#Welcome to Edgar's Beauty Store! --- Choose an item (1-3) or type 'done':
#   then check it against what really prints.