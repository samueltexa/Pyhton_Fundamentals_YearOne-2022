from Interfaces import options
def playAgain():
    playagain = input("""Do you wanna play again?(Yes/No)
Enter your option:""")
    if playagain.lower() == "yes":
        options.optionInterface()
    elif playagain.lower() == "no":
        print("Goodbye thanks")
    else:
        print("Wrong option chosen.")
        options.more_continue()
        options.optionInterface()