from data import MENU, resources
from os import system, name
from time import sleep


def clear_terminal():
    if name == 'nt':  # For Windows
        system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        system('clear')


def print_menu():
    """Prints the drink menu"""
    for drink in MENU.keys():
        print(drink)


def print_resources():
    """Prints the resources and the amount"""
    for resource, amount in resources.items():
        if resource == "Money":
            print(f"{resource.title()}    \t${amount}")
        else:
            if resource == "coffee":
                unit = 'g'
            else:
                unit = 'ml'
            print(f"{resource.title()}    \t{amount}{unit}")


def check_sufficient_resources(drink):
    """Checks if the coffee machine got sufficient resources for the drink"""
    ingredients = MENU[drink]['ingredients']
    missing_resources = False
    for resource, amount in ingredients.items():
        if resources.get(resource, 0) < amount:
            print(f'Sorry there is not enough {resource}')
            missing_resources = True
    return missing_resources


def make_drink(drink):
    """Makes the specified drink"""
    ingredients = MENU[drink]['ingredients']
    for resource, amount in ingredients.items():
        resources[resource] -= amount


def get_user_input():
    print('What would you like? (espresso/latte/cappuccino):')
    while True:
        answer = input("Input: ").lower()
        if answer == 'off':
            quit()
        elif answer == 'report':
            print_resources()
            return None
        elif answer in MENU.keys():
            return answer
        else:
            print('Invalid input!\n')


def process_coins(drink):
    cost = MENU[drink]['cost']
    try:
        penny = int(input("Enter the number of pennies: ")) * 0.01
        nickel = int(input("Enter the number of nickels: ")) * 0.05
        dime = int(input("Enter the number of dimes: ")) * 0.10
        quarter = int(input("Enter the number of quarters: ")) * 0.25

        # Input validation
        if any(coin < 0 for coin in [penny, nickel, dime, quarter]):
            raise ValueError("Number of coins cannot be negative.")
    except ValueError as err:
        print(f"Invalid input: {err}")
        return None

    total_amount = round(penny + nickel + dime + quarter, 2)
    if total_amount < cost:
        return None
    change = round(total_amount - cost, 2)
    if "Money" not in resources:
        resources['Money'] = 0
    resources['Money'] += cost
    return change


def main():
    while True:
        drink = get_user_input()
        if not drink:
            continue

        ingredients = check_sufficient_resources(drink)
        if not ingredients:
            continue

        change = process_coins(drink)
        if change is None:
            print(f'Not enough money to brew {drink}!')
            continue

        make_drink(drink)
        print(f"Here is your {drink}. Enjoy!")

        if change > 0:
            change = "{:.2f}".format(change)
            print(f"Here is your ${change} dollars in change")

        sleep(4)
        clear_terminal()


if __name__ == '__main__':
    main()
