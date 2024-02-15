# Strings and different methods of string concatitnation
"""
Strings are arrays====>Note I will talk about arrays later.
In computer programming, a string is a sequence of characters.
For example, "hello" is a string containing a sequence of
characters 'h' , 'e' , 'l' , 'l' , and 'o' . Here, we have
created a string variable named string1 . The variable is
initialized with the string Python Programming 
Strings can be either be represented using; double or single quotes as shown below"""

# Example1
string1 = "My name is samuel."
string2 = 'I come from the Alabama state.'
print(type(string1))
print(string1 + string2)
print(f"{string1} {string2}")
print("{} {}".format(string1,string2))

# Example2
name = "Samuel"
age = 21
place = "Alabama state"
like = "Skiing."
print("My name is", name, "I am", age ,"years old", "I come from", place, "and I like", like)
print("My name is "+name+"I am "+str(age)+"years old. I come from "+place+ "and I like "+like)
print(f"My name is {name} I am {age} years old I come from {place} and I like {like}")
print("My name is {} I am {} years old I come from {} and I like {}".format(name, age, place, like))

# Square brackets are used to access elements of a string.
# Example3
myName = "samuel"
print(myName[0]) # returns the letter at index 0
print(myName[1]) # returns the letter at index 1
print(myName[2]) # returns the letter at index 2
print(myName[0:2]) # returns the letter at index 0 and 1
print(myName[0:3]) # returns the letter at index 0, 1, and 2
print(myName[:3]) # returns the letter at index from 0 to 2
print(myName[:-1])
print(myName[-1:])
print(myName[-3:])
