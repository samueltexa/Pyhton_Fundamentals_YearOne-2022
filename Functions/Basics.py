# Defining a function
def myFunction1():
    print("This is my function.")
# Accessing the function
myFunction1()

# Sending information to functions
def myFunction2(greeting):
    print(greeting)
myFunction2("Hello how are you my friend?.")
myFunction2("I will beat you one day")

# Sending information or argument by keyword
def myFunction3(value1, value2):
    sum = value1 + value2
    print(f"The sum of value1 and value2 is {sum}")
myFunction3(3,5)
myFunction3(15,100)

# Giving a function argument a default value
def myFunction4(greeting = "How are you samuel?"):
    print(greeting)
myFunction4()
myFunction4("I will call you later")
    
# Creating functions with a variable number of arguments
def myFunction5(ArgumentCount, *numberOfTimes):
    print("You passed in ",ArgumentCount," arguments.")
    for Arguments in numberOfTimes:
        print(Arguments)      
myFunction5(1,"My name is samuel")        
myFunction5(2, "My name is samuel", "I come from Alabama state")

# Returning information from functions, Python functions can return;
# values
# varriables
# expressions
# results from other functions

def addition(value1, value2):
    sum = value1 + value2
    return sum
    # return value1 + value2
print("The sum of value1 and value2 is:",addition(2,4))

# comparing function output
print("3 + 4 equals 2 + 5 is", (addition(3, 4) == addition(2, 5)))
print((addition(3, 4) == addition(2, 6)))