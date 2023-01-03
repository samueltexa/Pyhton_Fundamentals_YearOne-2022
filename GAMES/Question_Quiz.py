def welcomeInerface():
    print("""Home Of Quiz Qustions
          Buttons
           Start
           Exit""")


def welcomeInterface():
    name = input("Provide your name to continue\nEnter your name:")
    print(f"Hello! {name}, welcome to a question quiz game.")


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
