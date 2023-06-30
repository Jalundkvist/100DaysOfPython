from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def setup():
    """ Creates the objects used in this OOP version of coffe machine"""
    menu = Menu()
    coffe_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    return menu, coffe_maker, money_machine


def report(coffe_maker, money_machine):
    coffe_maker.report()
    money_machine.report()


def main():
    menu, coffe_maker, money_machine = setup()
    while True:
        print(f'What would you like to order? {menu.get_items()}')
        choice = input('Input: ')
        if choice == 'off':
            quit()

        elif choice == 'report':
            report(coffe_maker, money_machine)

        else:
            drink = menu.find_drink(choice)
            if drink and coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
