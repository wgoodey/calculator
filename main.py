import art


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_number(side):
    number = ""
    while number == "":
        try:
            number = float(input(f"What's the {side} operand? "))
        except ValueError:
            print(f"{ENTER_VALID} number.")
    return number


def get_operation():
    mode = " "
    while mode not in operations:
        try:
            mode = input("Pick an operation ( + - * / ): ")
        except ValueError:
            print(f"{ENTER_VALID} option.")
    return mode


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Program start
print(art.logo)

quit_program = False
cleared = True

# OPERATIONS = "+-*/"
ENTER_VALID = "Please enter a valid"

result = 0
operator = ""

while not quit_program:
    if cleared:
        result = 0
        operator = ""
        left_side = get_number("left")
    else:
        left_side = result

    if cleared:
        operator = get_operation()

    right_side = get_number("right")

    # Perform operations
    if operator == "/" and right_side == 0:
        print("Cannot divide by 0.")
        result = left_side
        cleared = False
        continue
    else:
        calculation_function = operations[operator]
        result = calculation_function(left_side, right_side)
        print(f"{left_side} + {right_side} = {result}")

    # Get next step
    while True:
        print("What next? (C)lear, E(x)it, or perform an operation on current result ( + - * / ): ")
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
                operator = next_step
                break
        except IndexError:
            print(f"{ENTER_VALID} option.")
