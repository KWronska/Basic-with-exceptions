# Calculator functions

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# user input
def user_input():
    try:
        a = float(input("Please give me the first number: "))
        b = float(input("Please give me the second number: "))
        symbol = input("What you want me to do? +, -, *, / : ")

        if symbol in list("+, -, *, /"):
            return a, b, symbol

    except ValueError:
        print("Invalid data type for number.")


# when to use which function with output from user_input func
def calculator(output):
    try:
        a = output[0]
        b = output[1]
        symbol = output[2]

        if symbol == "+":
            result = add(a, b)
        elif symbol == "-":
            result = sub(a, b)
        elif symbol == "*":
            result = mul(a, b)
        elif symbol == "/":
            result = div(a, b)
        return result
    except UnboundLocalError:
        print("Check your spelling, dude. Restart please.")


again = input("Hello write 'OK' to start calculation!\n").lower()

if again != 'ok' and again != 'yes':
    print("Okay, see you next time.")
else:
    try:
        while again == 'yes' or again == 'ok':
            output = user_input()
            output = list(output)
            final = calculator(output)

            print(f"Your operation:\n {output[0]} {output[2]} {output[1]} = {final}\n")

            again = input("Do you want to calculate again? [yes, no]: ").lower()
            print("\n")

        if again == 'no':
            print("Bye, bye")
    except TypeError:
        print("You caused an Error, bye bye.")
