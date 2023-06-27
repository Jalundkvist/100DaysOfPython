from data import MENU, resources


def print_menu():
    """Prints the drink menu"""
    for drink in MENU.keys():
        print(drink)


def print_resources():
    """Prints the resources and the amount"""
    for resource, amount in resources.items():
        if resource == "coffee":
            unit = 'g'
        else:
            unit = 'ml'
        print(f"Resource: {resource}  \t{amount}{unit} left")


def check_sufficient_resources(drink):
    """Checks if the coffee machine got sufficient resources for the drink"""
    ingredients = MENU[drink]['ingredients']
    for resource, amount in ingredients.items():
        if resources.get(resource, 0) < amount:
            return False
    for resource, amount in ingredients.items():
        resources[resource] -= amount
    return True


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


def count_coins(drink):
    return drink


# TODO: Process coins.\
""" a. If there are sufficient resources to make the drink selected, then the program should
        prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
 """
# TODO: Check transaction successful? I.G Offer change if too much .2f

# TODO: Make Coffee.


def main():
    print_menu()
    print_resources()
    drink = get_user_input()
    print(drink)
    if check_sufficient_resources(drink):
        count_coins(MENU[drink]['cost'])
        

if __name__ == '__main__':
    main()
