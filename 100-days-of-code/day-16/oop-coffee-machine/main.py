from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):").lower()

    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        if not money_machine.make_payment(drink.cost):
            continue
        coffee_maker.make_coffee(drink)
    else:
        print("Invalid input")
