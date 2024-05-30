from prettytable import PrettyTable

class Menu:
    def __init__(self):
        self.menu = {
            "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 1.5},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
        }

class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
        self.menu = Menu().menu
        self.is_on = True

    def report(self):
        table = PrettyTable()
        table.field_names = ["Resource", "Amount"]
        for resource, amount in self.resources.items():
            unit = "ml" if resource in ["water", "milk"] else "g" if resource == "coffee" else ""
            table.add_row([resource.capitalize(), f"{amount}{unit}"])
        print(table)

    def check_resources(self, drink):
        for ingredient, required_amount in self.menu[drink]["ingredients"].items():
            if self.resources[ingredient] < required_amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickels + pennies
        return total

    def check_transaction(self, money_received, drink):
        cost = self.menu[drink]["cost"]
        if money_received >= cost:
            change = round(money_received - cost, 2)
            self.resources["money"] += cost
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink):
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            self.resources[ingredient] -= amount
        print(f"Here is your {drink}. Enjoy!")

    def run(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.check_resources(choice):
                    print(f"The cost of a {choice} is ${self.menu[choice]['cost']:.2f}.")
                    money_received = self.process_coins()
                    if self.check_transaction(money_received, choice):
                        self.make_coffee(choice)
            else:
                print("Invalid input. Please choose from espresso, latte, or cappuccino.")

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()
