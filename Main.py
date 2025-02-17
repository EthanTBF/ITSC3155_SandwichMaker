### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, there's not enough {item}")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert money.")
        large_dollars = int(input("How many large dollars? ($1): ")) * 1.00
        half_dollars = int(input("How many half dollars? ($0.50): ")) * 0.5
        quarters = int(input("How many quarters? ($0.25): ")) * 0.25
        nickels = int(input("How many nickels? ($0.05): ")) * 0.05
        return large_dollars + half_dollars + quarters + nickels


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print(f"Sorry, there's not enough money, money refunded.")
            return False
        elif coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here's ${change} in change.")
            return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/medium/large/report/off): ")
    if choice == "off":
        break
    elif choice == "report":
        for item, amount in resources.items():
            unit = "slice(s)" if item != "cheese" else "pound(s)"
            print(f"{item}: {amount} {unit}")
    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            coins_inserted = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins_inserted, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])