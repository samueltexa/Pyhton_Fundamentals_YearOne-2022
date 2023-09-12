import user, more_Continue
def continueInterface():
    proceed = input("Do you want to continue?(Yes/No)\nEnter your option:")
    if proceed.lower() == "yes":
        user.userInterface()
    elif proceed.lower() == "no":
        print("Thanks, see you again.")
        import sys
        sys.exit()
    else:
        print("You have chosen wrong option.")
        more_Continue.more_continue()
        # import sys
        # sys.exit()