KEY_ESPRESSO = "espresso"
KEY_LATTE = "latte"
KEY_CAPPUCCINO = "cappuccino"
KEY_INGREDIENTS = "ingredients"

MENU = {
    KEY_ESPRESSO: {
        KEY_INGREDIENTS: {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
        "emoji": "☕"
    },
    KEY_LATTE: {
        KEY_INGREDIENTS: {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "emoji": "🥛"
    },
    KEY_CAPPUCCINO: {
        KEY_INGREDIENTS: {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "emoji": "☕"
    }
}


def get_menu_items():
    menu_items = []
    for key in MENU:
        menu_items.append(key)
    return menu_items


def get_ingredients_by_drink(drink_name):
    return MENU[drink_name]["ingredients"]


def is_resource_sufficient(resources, drink):
    for item, quantity in MENU[drink][KEY_INGREDIENTS].items():
        if quantity > resources[item]:
            return f"Sorry there is not enough {item}.\n"
    return ""


def is_transaction_successful(mooney_inserted, drink):
    return mooney_inserted - MENU[drink]["cost"]


def make_drink(resources, drink, mooney):
    mooney += MENU[drink]["cost"]
    for item, quantity in resources.items():
        if item in MENU[drink][KEY_INGREDIENTS]:
            resources[item] -= MENU[drink][KEY_INGREDIENTS][item]
    return mooney

def get_drink_emojy(drink):
    return MENU[drink]["emoji"]
