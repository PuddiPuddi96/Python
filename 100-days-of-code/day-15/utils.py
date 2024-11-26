coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

def process_coins():
    coins_inserted = {}
    for coin in coins:
        coin_number = int(input(f"How many {coin}? "))
        coins_inserted[coin] = coin_number

    return coins_inserted

def calculate_total_coins(coins_inserted):
    amount = 0
    for coin, number_coins in coins_inserted.items():
        amount += coins[coin] * number_coins
    return amount
