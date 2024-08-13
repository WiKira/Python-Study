from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def in_process(drink, coffee_maker, money_machine):
    if coffee_maker.is_resource_sufficient(drink) is False and money_machine.make_payment(drink.cost) is False:
        return

    coffee_maker.make_coffee(drink)


def machine_on():
    """Process running while the machine is on"""
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    options = menu.get_items().split('/')
    while 1 == 1:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        match choice:
            case "off":
                return
            case "report":
                coffee_maker.report()
                money_machine.report()
            case _:
                if choice not in options:
                    print("Invalid command. Please try again.")
                    continue

                in_process(menu.find_drink(choice),
                           coffee_maker,
                           money_machine)


machine_on()
print("Good bye!")
