from menu import get_menu_items, is_resource_sufficient, is_transaction_successful, make_drink, get_drink_emojy
from utils import process_coins, calculate_total_coins


resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
}

profit = 0


COMMAND_OFF = "off"
COMMAND_REPORT = "report"


def get_report():
    report = ""
    for key in resources:
        if key != "coffee":
            report += f"{key}: {resources[key]}ml\n"
        else:
            report += f"{key}: {resources[key]}g\n"
    report += f"Mooney: ${profit}"
    return report


menu_items = get_menu_items()
is_on = True

while is_on:
    choice = input(f"What would you like? ({'\\'.join(menu_items)}):").lower()
    if choice == COMMAND_OFF:
        print("Goodbye!")
        is_on = False
    elif choice == COMMAND_REPORT:
        print(get_report())
    elif choice in menu_items:
        resource_message = is_resource_sufficient(resources, choice)
        if resource_message != "":
            print(resource_message)
            continue

        print("Please insert coins.")
        coins_inserted = process_coins()
        payment = calculate_total_coins(coins_inserted)

        change = round(is_transaction_successful(payment, choice), 2)
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            continue

        profit = make_drink(resources, choice, profit)

        print(f"Here is ${change} dollars in change.\nHere is your {choice}. Enjoy! {get_drink_emojy(choice)}")
    else:
        print("Invalid input")
