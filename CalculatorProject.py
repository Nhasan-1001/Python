import sys

from colorama import Fore, Style


# This function is for addition of two number
def add():
    try:
        num1 = float(input(Fore.LIGHTGREEN_EX + "Enter first number: " + Style.RESET_ALL))
        num2 = float(input(Fore.LIGHTGREEN_EX + "Enter second number: " + Style.RESET_ALL))
        print(num1, "+", num2, "=", num1 + num2)
        print(Fore.LIGHTYELLOW_EX + f"RESULT: {(num1 + num2)}" + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")

    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")


# This function subtracts two numbers
def subtract():
    try:
        num1 = float(input(Fore.LIGHTGREEN_EX + "Enter first number: " + Style.RESET_ALL))
        num2 = float(input(Fore.LIGHTGREEN_EX + "Enter second number: " + Style.RESET_ALL))
        print(num1, "-", num2, "=", num1 - num2)
        print(Fore.LIGHTYELLOW_EX + f"RESULT: {(num1 - num2)}" + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")


# This function multiplies two numbers
def multiply():
    try:
        num1 = float(input(Fore.LIGHTGREEN_EX + "Enter first number: " + Style.RESET_ALL))
        num2 = float(input(Fore.LIGHTGREEN_EX + "Enter second number: " + Style.RESET_ALL))
        print(num1, "*", num2, "=", num1 * num2)
        print(Fore.LIGHTYELLOW_EX + f"RESULT: {(num1 * num2)}" + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")


# This function divides two numbers
def divide():
    try:
        num1 = float(input(Fore.LIGHTGREEN_EX + "Enter first number: " + Style.RESET_ALL))
        num2 = float(input(Fore.LIGHTGREEN_EX + "Enter second number: " + Style.RESET_ALL))
        if num2 != 0.0:
            print(num1, "/", num2, "=", num1 / num2)
            print(Fore.LIGHTYELLOW_EX + f"RESULT: {(num1 / num2)}" + Style.RESET_ALL)
            print("++++++++++++++++++++++++++++++++++++")
        else:
            print(Fore.RED + "The fist number could not be divided by zero" + Style.RESET_ALL)
            print("++++++++++++++++++++++++++++++++++++")

    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")


# This function for exponent calculation of one number
def exponent():
    try:
        x = float(input(Fore.LIGHTGREEN_EX + "Enter the NUMBER : " + Style.RESET_ALL))
        y = int(input(Fore.LIGHTGREEN_EX + "Enter the EXPONENT: " + Style.RESET_ALL))
        mul = 1
        for i in range(int(y)):
            mul = mul * x
        print("The power of", x, "^", y, " = ", mul)
        print(Fore.LIGHTYELLOW_EX + f"RESULT: {mul}" + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a float number for NUMBER and whole-number for EXPONENT."
              + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")


# This function will stop the calculator
def termination():
    print("++++++++++++++++++++++++++++++++++++")
    print()
    sys.exit(Fore.RED + "CALCULATOR STOPPED SUCCESSFULLY!" + Style.RESET_ALL)


# This function will display the main menu of my calculator
def display():
    print(Fore.RED + "|==================================|" + Style.RESET_ALL)
    print(Fore.RED + "| " + Style.RESET_ALL + Fore.LIGHTBLUE_EX + "           CALCULATOR           " + Style.RESET_ALL
          + Fore.RED + " |" + Style.RESET_ALL)
    print(Fore.RED + "|==================================|" + Style.RESET_ALL)

    print(" SELECT an OPERATION from the MENU:")
    print(Fore.RED + "||================================||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "1.ADDITION                      " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "2.SUBTRACTION                   " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "3.MULTIPLICATION                " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "4.DIVISION                      " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "5.EXPONENTION                   " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||" + Style.RESET_ALL + Fore.GREEN + "6.EXIT                          " + Style.RESET_ALL
          + Fore.RED + "||" + Style.RESET_ALL)
    print(Fore.RED + "||================================||" + Style.RESET_ALL)


while True:
    display()
    # take input from the user
    choice = input("\n""Enter a CHOICE (1/2/3/4/5/6):  ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):

        if choice == '1':
            add()

        elif choice == '2':
            subtract()

        elif choice == '3':
            multiply()

        elif choice == '4':
            divide()

        elif choice == '5':
            exponent()

        elif choice == '6':
            termination()

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("PRESS any KEY for CONTINUE or NO for STOP: ")
        if next_calculation == "n" or next_calculation == "N" or next_calculation == "NO" or next_calculation == "no" \
                or next_calculation == "No" or next_calculation == "nO":
            termination()

    else:
        print(Fore.RED + "Invalid Input! Please give the choice properly." + Style.RESET_ALL)
        print("++++++++++++++++++++++++++++++++++++")
