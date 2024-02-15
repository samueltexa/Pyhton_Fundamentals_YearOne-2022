"""A variable is a label that can be assigned to a value. And a variable is always
associated with a value. Variables are used to store values"""

numbers = [1,2,3,4]
sting_numbers = [str(i) for i in numbers]
joinstring = " ".join(sting_numbers)
print(joinstring)
print(type(joinstring))

meassage = "Hello how are over there"
print(meassage)

name  = "samuel"
meassage = "Hello"
print(f"{meassage} {name}")

meassage1 = f"How are you{name}"
print(meassage1)