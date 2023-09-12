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