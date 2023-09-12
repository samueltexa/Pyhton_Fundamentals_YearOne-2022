def userInterface():
    try:
        name = input("Enter your name to continue: ")
        for i in name:
            int(i)
            print("Next time enter only string values")
    except:
            print(f"Hello {name} welcome to a logical calculator.")
            #continueInterface()



