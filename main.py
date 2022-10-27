import art


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_input(side):
    number = ""
    while number == "":
        try:
            number = float(input(f"What's the {side} operand? "))
        except ValueError:
            print(f"{ENTER_VALID} number.")
    return number


def get_operation():
    mode = " "
    while mode not in OPERATIONS:
        try:
            mode = input("Pick an operation ( + - * / ): ")
        except ValueError:
            print(f"{ENTER_VALID} option.")
    return mode

# Program start
print(art.logo)

quit_program = False
cleared = True

OPERATIONS = "+-*/"
ENTER_VALID = "Please enter a valid"

result = 0
operation = ""

while not quit_program:
    if cleared:
        result = 0
        operation = ""
        num1 = get_input("left")
    else:
        num1 = result

    if cleared:
        operation = get_operation()

    num2 = get_input("right")

    # Perform operations
    if operation == "+":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    else:
        if num2 != 0:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Cannot divide by 0.")
            result = num1
            cleared = False
            continue

    # Get next step
    while True:
        print("What next? (C)lear, E(x)it, or Pick an operation ( + - * / ): ")
        try:
            next_step = input(f"{result} ").upper()
            next_step = next_step[0]
            if next_step == "X":
                quit_program = True
                break
            elif next_step == "C":
                cleared = True
                break
            elif next_step == "N":
                cleared = False
                break
            else:
                cleared = False
                operation = next_step
                break
        except IndexError:
            print(f"{ENTER_VALID} option.")

