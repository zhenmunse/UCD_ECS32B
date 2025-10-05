from muffin import Muffin
from drink import Drink

class Bakery:
    def __init__(self):
        self.display_case = []
        self.muffin_menu = {}  # Dictionary for muffins
        self.drink_menu = {}   # Dictionary for drinks
        self.money = 0.0
        self.sales = []

    def stock_bakery(self, items):  # items is a list of Muffin and Drink objects
        for item in items:
            self.display_case.append(item)  # Add item to display case
            if isinstance(item, Muffin) and item.flavor not in self.muffin_menu: # Avoid duplicates 
                self.muffin_menu[item.flavor] = item.price
            elif isinstance(item, Drink) and item.type not in self.drink_menu:  # Avoid duplicates
                self.drink_menu[item.type] = item.price

    def fill_order(self, order_item):
        for item in self.display_case:  # Look for the item in the display case
            if isinstance(item, Muffin) and item.flavor == order_item:  # Match by flavor, if the instance has attribute flavor it is a Muffin
                self.sales.append(item.flavor)
                self.money += item.price
                self.display_case.remove(item)
                if item not in self.display_case: # Remove from menu if out of stock
                    self.muffin_menu.pop(item.flavor, None)
                print(f"Order filled: {item.flavor}. Price: ${item.price:.2f}")
                return
            elif isinstance(item, Drink) and item.type == order_item: # Match by type, same duck typing logic
                self.sales.append(item.type)
                self.money += item.price
                self.display_case.remove(item)
                if item not in self.display_case:   # Remove from menu if out of stock
                    self.drink_menu.pop((item.size, item.type), None)
                print(f"Order filled: {item.type}. Price: ${item.price:.2f}")
                return
            print(f"Sorry, {order_item} is out of stock.")

    def display_menu(self):
        print("Muffin Menu:")
        for muffin, price in self.muffin_menu.items(): # muffin is this flavor
            print(f"{muffin}: ${price:.2f}")
        print()
        print("Drink Menu:")
        for drink, price in self.drink_menu.items():  # drink is this type
            print(f"{drink}: ${price:.2f}")
        print()

    def daily_summary(self):
        print(f"Total sales today: ${self.money:.2f}")
        print("Items sold:")
        for item in self.sales:
            print(item)
     

def run_bakery():
    bakery = Bakery()

    # Stock the bakery with some muffins and drinks
    muffins = [
        Muffin("blueberry", 2.50),
        Muffin("chocolate", 3.00),
    ]
    drinks = [
        Drink("medium", "coffee", 1.75),
        Drink("large", "tea", 2.00),
    ]

    bakery.stock_bakery(muffins + drinks)

    # Display the menu
    bakery.display_menu()

    # Fill some example orders
    bakery.fill_order("blueberry")
    bakery.fill_order("coffee")
    
    print()

    # Show the updated menu and daily summary
    bakery.display_menu()
    bakery.daily_summary()

# Example usage
if __name__ == "__main__":
    run_bakery()