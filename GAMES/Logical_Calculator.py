from ast import Str


def welcomeInterface():
    print("""<=====WELCOME TO A LOGICAL CALCULATOR=====>
                 ACTIONS
            Yes to continue
            No to exit""")

def userInterface():
    try:
        name = input("Enter your name to continue: ")
        for i in name:
            int(i)
            print("Next time enter only string values")
    except:
            print(f"Hello {name} welcome to a logical calculator.")
            #continueInterface()


def continueInterface():
    proceed = input("Do you want to continue?(Yes/No)\nEnter your option:")
    if proceed.lower() == "yes":
        userInterface()
    elif proceed.lower() == "no":
        print("Thanks, see you again.")
        import sys
        sys.exit()
    else:
        print("You have chosen wrong option.")
        more_continue()
        # import sys
        # sys.exit()


def more_continue():
    more = input("Do you wanna try again?.(Yes/No)\nEnter your option.")
    if more.lower() == "yes":
        userInterface()
    elif more.lower() == "no":
        print("Goodbye, see you again soon.")
        import sys
        sys.exit()
    else:
        print("Wrong option chosen.")
        import sys
        sys.exit()


def playAgain():
    playagain = input("""Do you wanna play again?(Yes/No)
Enter your option:""")
    if playagain.lower() == "yes":
        optionInterface()
    elif playagain.lower() == "no":
        print("Goodbye thanks")
    else:
        print("Wrong option chosen.")
        more_continue()
        optionInterface()


def optionInterface():
    print("Choose your option below.")
    choose = input("""(a).Multiplication\n(b).Addition
(c).Subtruction\n(d).Modulus\nEnter your option:""")
    if choose.lower() == "a":
        choose1 = input("""You have chosen Multiplication, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose1.lower() == "yes":
            multiplication()
        elif choose1.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            playAgain()
    elif choose.lower() == "b":
        choose2 = input("""You have chosen Addition, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose2.lower() == "yes":
            addition()
        elif choose2.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            playAgain()
    elif choose.lower() == "c":
        choose3 = input("""You have chosen Subtruction, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose3.lower() == "yes":
            subtruction()
        elif choose3.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            playAgain()
    elif choose.lower() == "d":
        choose4 = input("""You have chosen Modlus, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose4.lower() == "yes":
            modulus()
        elif choose4.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from above options.")
            playAgain()
    else:
        print("Choose from the above options.")
        playAgain()


def addition():
    x = 0
    while x <= 2:
        num1 = input("Enter first number:")
        num2 = input("Enter second number:")
        try:
            number1 = int(num1)
            number2 = int(num2)
            sum = number1 + number2
            print(f"The sum is {sum}")
            playAgain()
            import sys
            sys.exit()
        except ValueError:
            print("Only numbers accepted.")
            x += 1
    print("Maximum trials reached, you can try again later.")


def multiplication():
    x = 0
    while x <= 2:
        num1 = input("Enter first number:")
        num2 = input("Enter second number:")
        try:
            number1 = int(num1)
            number2 = int(num2)
            product = number1 * number2
            print(f"The product is {product}")
            playAgain()
            import sys
            sys.exit()
        except ValueError:
            print("Only numbers accepted.")
            x += 1
    print("Maximum trials reached, you can try again later.")


def subtruction():
    x = 0
    while x <= 2:
        num1 = input("Enter first number:")
        num2 = input("Enter second number:")
        try:
            number1 = int(num1)
            number2 = int(num2)
            difference = number1 - number2
            print(f"The difference is {difference}")
            playAgain()
            import sys
            sys.exit()
        except ValueError:
            print("Only numbers accepted.")
            x += 1
    print("Maximum trials reached, you can try again later.")


def modulus():
    x = 0
    while x <= 2:
        num1 = input("Enter first number:")
        num2 = input("Enter second number:")
        try:
            number1 = int(num1)
            number2 = int(num2)
            modulus = number1 % number2
            print(f"The modulus is {modulus}")
            playAgain()
            import sys
            sys.exit()
        except ValueError:
            print("Only numbers accepted.")
            x += 1
    print("Maximum trials reached, you can try again later.")


def main():
    welcomeInterface()
    continueInterface()
    optionInterface()
    # playAgain()


if __name__ == '__main__':
    main()
