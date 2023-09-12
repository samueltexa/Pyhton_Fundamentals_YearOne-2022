import PlayAgain
def optionInterface():
    print("Choose your option below.")
    choose = input("""(a).Multiplication\n(b).Addition
(c).Subtruction\n(d).Modulus\nEnter your option:""")
    if choose.lower() == "a":
        choose1 = input("""You have chosen Multiplication, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose1.lower() == "yes":
           imports.operations.Multiplication.multiplications.multiplication()
        elif choose1.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            PlayAgain.playAgain()
    elif choose.lower() == "b":
        choose2 = input("""You have chosen Addition, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose2.lower() == "yes":
            imports.operations.Addition.addition.addition()
        elif choose2.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            PlayAgain.playAgain()
    elif choose.lower() == "c":
        choose3 = input("""You have chosen Subtruction, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose3.lower() == "yes":
            imports.operations.Subtraction.Subtractions.subtruction()
        elif choose3.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from the above options.")
            PlayAgain.playAgain()
    elif choose.lower() == "d":
        choose4 = input("""You have chosen Modlus, Do you want to continue?(Yes/No)
Enter your option:""")
        if choose4.lower() == "yes":
            imports.operations.Modulus.modulus.modulus()
        elif choose4.lower() == "no":
            print("Nice to have you here goodbye.")
        else:
            print("Choose from above options.")
            PlayAgain.playAgain()
    else:
        print("Choose from the above options.")
        PlayAgain.playAgain()