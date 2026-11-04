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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def machine_report():
    """
    Prints a current report of the machine's resources.
    """
    resource_values = ["Water: ", "Milk: ", "Coffee: "]
    resource_labels = ["ml ", "ml" , "g"]
    i = 0
    for amounts in list(resources.values())[0:3]:
        print(f"{resource_values[i]}{amounts}{resource_labels[i]}")
        i += 1
    print(f"Money: ${resources['money'] / 100:.2f}")

def resource_checker(user_choice_check):
    """
    Checks whether the machine has enough of every ingredient for a drink.
    :param user_choice_check: The drink the customer ordered.
    :return: True if every ingredient is in stock,
    otherwise False(after printing which one is short).
    """
    for name,resources_drink in MENU[user_choice_check]["ingredients"].items():
        if resources[name] < resources_drink:
            print(f"Not enough {name}!")
            return False
    return True

def coin_insert(drink_cost_var):
    """
    Lets the customer insert coins until the drink is paid for, or they stop.
    :param drink_cost_var: The price of the drink in cents.
    :return:The cents still owed. Positive means not enough was paid, 0 means exact,
    negative means they overpaid (the change).
    """
    user_coin_input = 0
    user_coin_decision = "y"
    print(f"Your drink is {drink_cost_var} cents.")
    while user_coin_decision != "n":
        while user_coin_input < drink_cost_var:
            user_coin_decision = input("Do you want to enter coins? (y/n) ").lower()
            coin_choice = input("What coin do you want to insert?")
            if coin_choice == "quarters":
                quarters = int(input("How many quarters do you want to insert? "))
                user_coin_input += (quarters * 25)
                drink_cost_var -= user_coin_input
                user_coin_input = 0
                print(f"{drink_cost_var} cents remaining.")
                if drink_cost_var <= 0:
                    break
                user_coin_decision = input("Do you want to enter coins? (y/n) ").lower()
                if user_coin_decision == "n" or drink_cost_var <= 0:
                    break
            elif coin_choice == "dimes":
                dimes = int(input("How many dimes do you want to insert? "))
                user_coin_input += (dimes * 10)
                drink_cost_var -= user_coin_input
                user_coin_input = 0
                print(f"{drink_cost_var} cents remaining.")
                if drink_cost_var <= 0:
                    break
                user_coin_decision = input("Do you want to enter coins? (y/n) ").lower()
                if user_coin_decision == "n" or drink_cost_var <= 0:
                    break
            elif coin_choice == "nickels":
                nickels = int(input("How many nickels do you want to insert? "))
                user_coin_input += (nickels * 5)
                drink_cost_var -= user_coin_input
                user_coin_input = 0
                print(f"{drink_cost_var} cents remaining.")
                if drink_cost_var <= 0:
                    break
                user_coin_decision = input("Do you want to enter coins? (y/n) ").lower()
                if user_coin_decision == "n" or drink_cost_var <= 0:
                    break
            elif coin_choice == "pennies":
                pennies = int(input("How many pennies do you want to insert? "))
                user_coin_input += (pennies * 1)
                drink_cost_var -= user_coin_input
                user_coin_input = 0
                print(f"{drink_cost_var} cents remaining.")
                if drink_cost_var <= 0:
                    break
                user_coin_decision = input("Do you want to enter coins? (y/n) ").lower()
                if user_coin_decision == "n" or drink_cost_var <= 0:
                    break
        break
    return drink_cost_var

def drink_payment(remaining_payment, user_choice_var, drink_cost_profit):
    """
    Takes the inputted money from the customer and adds it to the machine's money.
    Gives them change if they inputted too much or refunds if they did not input enough.
    :param remaining_payment: How much money remaining after the customer has finished inputted their money.
    :param user_choice_var: The drink the customer ordered.
    :param drink_cost_profit: The price of the drink in cents, added to the machine's money.
    """
    if remaining_payment > 0:
        print("Sorry that's not enough money. Money refunded.")
    elif remaining_payment < 0:
        print(f"Here is ${round(remaining_payment * -1 / 100, 2)} in change.")
        print(f"Enjoy your {user_choice_var}!")
        resources["money"] += drink_cost_profit
        subtract_ingredients(user_choice_var)
    else:
        print(f"Enjoy your {user_choice_var}!")
        resources["money"] += drink_cost_profit
        subtract_ingredients(user_choice_var)

def subtract_ingredients(user_choice_check):
    """
    Subtracts ingredients from the machine.
    :param user_choice_check: The drink the customer ordered.
    """
    for name, resources_drink in MENU[user_choice_check]["ingredients"].items():
        resources[name] = (resources[name] - resources_drink)

def refill_machine():
    """
    Allows the user to add more ingredients to the machine.
    """
    refill_name = input("What ingredient do you want to refill? Milk/Water/Coffee ").lower()
    if refill_name == "water" or refill_name == "coffee" or refill_name == "milk":
        amount = resources[refill_name]
        print(f"You have {amount} {refill_name} currently")
        try:
            refill_num = int(input(f"How much {refill_name} do you want to add? "))
            if refill_num >= 0:
                confirm_refill = input(f"Refill {refill_name} {refill_num}? (y/n) ")
                if confirm_refill == "y":
                    resources[refill_name] += refill_num
                    print(f"You have {resources[refill_name]} {refill_name} now.")
                else:
                    print("Exiting.")
            else:
                print("Cannot add a negative number!")
        except ValueError:
            print("Please enter a number!")
    else:
        print("That is not an ingredient!")

#Machine Workflow
user_choice = "default"
drink_cost = 0
while user_choice != "off":
    drink_cost = 0
    user_choice = input("What would you like? (espresso/latte/cappuccino) ")
    if user_choice == "report":
        machine_report()
    elif user_choice == "refill":
        refill_machine()
    elif user_choice == "espresso":
        result = resource_checker(user_choice)
        if result == True:
            drink_cost = (round(MENU[user_choice]["cost"] * 100))
            remaining = coin_insert(drink_cost)
            drink_payment(remaining, user_choice, drink_cost)

    elif user_choice == "latte":
        result = resource_checker(user_choice)
        if result == True:
            drink_cost = (round(MENU[user_choice]["cost"] * 100))
            remaining = coin_insert(drink_cost)
            drink_payment(remaining, user_choice, drink_cost)

    elif user_choice == "cappuccino":
        result = resource_checker(user_choice)
        if result == True:
            drink_cost = (round(MENU[user_choice]["cost"] * 100))
            remaining = coin_insert(drink_cost)
            drink_payment(remaining, user_choice, drink_cost)

print("Machine Off")



