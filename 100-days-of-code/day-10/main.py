from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)
to_continue = True
should_accumulate = False

while to_continue:
    if not should_accumulate:
        n_1 = float(input("Chose the first number: "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    n_2 = float(input("Chose the second number: "))

    result = operations[operation](n_1, n_2)
    print(f"{n_1} {operation} {n_2} = {result}")

    choice = input("Continue with the previous result? y/n:")
    if choice == "y":
        n_1 = result
        should_accumulate = True
    else:
        should_accumulate = False
        stop_calculator = input("Continue with the calculator? y/n:")
        if stop_calculator == "n":
            to_continue = False
