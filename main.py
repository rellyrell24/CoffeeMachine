MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": { 
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profits = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    # "tea": 70,
}


def is_transaction_successful(amount_received, cost_of_drink):
    """Return true when payment is accepted, false when insufficient"""
    if amount_received >= cost_of_drink:
        change = round(amount_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profits
        profits += cost_of_drink
        return True
    else:
        print("Sorry that is not enough money. Coins refunded")
        return False


def is_resource_sufficient(order_ingredients):
    """Return whether there is enough resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickel?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is you {drink_name} ☕️")

is_on = True

while is_on:
    # TODO: 1. Prompt user by asking "What would you like?"
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off machine by typing "off" to the prompt
    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO: 3. Print the report
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profits}")
    else:
        # TODO: 4. Check resource sufficient?
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # TODO 5. Process coins
            payment = process_coins()
            # TODO 6. Check transaction was successful
            if is_transaction_successful(payment, drink["cost"]):
                # TODO 7. Make Coffee
                make_coffee(choice, drink["ingredients"])


