# Design a system to manage a restaurant menu, including items, prices, categories,
# and the ability to display and update the menu.

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def updatePrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class RestaurantMenu:
    def __init__(self):
        self.menu = []

    def addItem(self, item):
        self.menu.append(item)

    def removeItem(self, item_name):
        self.menu = [item for item in self.menu if item.name != item_name]

    def update_item_price(self, item_name, new_price):
        for item in self.menu:
            if item.name == item_name:
                item.updatePrice(new_price)
                return f"Price of '{item_name}' updated to ${new_price:.2f}"
        return "Item not found."

    def display_menu(self):
        if not self.menu:
            print("Menu is empty.")
            return

        categories = {}
        for item in self.menu:
            categories.setdefault(item.category, []).append(item)

        print("\nRestaurant Menu:")
        for category, items in categories.items():
            print(f"\n{category}:")
            for item in items:
                print(f" - {item}")


# Example usage:
obj = RestaurantMenu()

obj.addItem(MenuItem("Burger", 5.99, "Fast Food"))
obj.addItem(MenuItem("Pizza", 8.99, "Fast Food"))
obj.addItem(MenuItem("Coke", 1.99, "Beverages"))
obj.addItem(MenuItem("Coffee", 2.49, "Beverages"))

obj.display_menu()

print("\nUpdating Price:")
print(obj.update_item_price("Pizza", 9.49))

obj.display_menu()

print("\nRemoving Item:")
obj.removeItem("Coke")
obj.display_menu()