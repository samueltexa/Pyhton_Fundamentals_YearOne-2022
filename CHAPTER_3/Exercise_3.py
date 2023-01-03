try:
    score = float(input("Enter your score:"))
    if 0.0 < score < 100.0:
        if score >= 80.0:
            print("A")
        elif score >= 70.0:
            print("B")
        elif score >= 60.0:
            print("C")
        elif score >= 50.0:
            print("D")
        elif score < 50.0:
            print("F")
    else:
        print("Bad score.")
except ValueError:
    print("Bad score.")
