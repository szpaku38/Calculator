from art import logo
print(logo)


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

is_on = True

num1 = int(input("What's the first number? "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

while is_on:
    num2 = int(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    next_calc = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

    if next_calc == "n":
        is_on = False
    else:
        num1 = answer
        operation_symbol = input("Pick an operation: ")
