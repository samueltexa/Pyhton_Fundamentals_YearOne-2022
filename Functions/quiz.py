def welcomeInerface():
    print(
        """<========Home Of Quiz Questions=======>
Enter Start to continue and Exit to Exit
            Start
            Exit""")
    start_game()
    
def start_game():
    option = input("Enter your option here: ")
    if option == "start":
        nameInterface()
        import sys
        sys.exit()
    if option == "exit":
        exit()
    else:
        print("Invalid option chosen.")
        
def exit():
    print("Thaks for passing by, hope to see you soon.")

def nameInterface():
    name = input("Provide your name to continue\nEnter your name:")
    print(f"Hello! {name}, welcome to a question quiz game.")
    print("Please answer the questions below.")
    question1()
    question()


def question1():
    question1 = input("What is the capital of Uganda?\nEnter your answer:")
    try:
        if question1.lower() == "kampala":
            print("Thats correct.")
        else:
            print("Thats wrong answer.")
    except NameError:
        print("Gabbage entered")


def question():
    question3 = input("Who led Uganda to independence?\nEnter your answer:")
    try:
        if question3.lower() == "Obote".lower():
            print("Wow! you got it right correct.")
        else:
            print("Thats wrong answer.")
    except NameError:
        print("Gabbage entered")

welcomeInerface()
