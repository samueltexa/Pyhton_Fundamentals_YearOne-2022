import user
def more_continue():
    more = input("Do you wanna try again?.(Yes/No)\nEnter your option.")
    if more.lower() == "yes":
        user.userInterface()
    elif more.lower() == "no":
        print("Goodbye, see you again soon.")
        import sys
        sys.exit()
    else:
        print("Wrong option chosen.")
        import sys
        sys.exit()