"""The list is a versatile data type exclusive in Python. In a sense,
it is the same as the array in C/C++. But the interesting thing
about the list in Python is it can simultaneously hold different
types of data. Formally list is an ordered sequence of some data
written using square brackets([]) and commas(,)."""

# Example
#list of having only integers
a= [1,2,3,4,5,6]
print(a)

#list of having only strings
b=["hello","john","reese"]
print(b)

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)

#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c

print(a,b)
print(c[0], b[1])

"""Working with Lists and different operations performed on lists"""
# Ways to modify a pyton list.
""" Append method, Remove method, Pop method, Insert method, Sort method, Index method, Count method,
Extend method"""

"""Example"""
# Defining list
list = ["jack", "emma", "Dani", "Samuel", "Karen", "Karen"]
print(list)
list[0] = "Eddy" # Update the item at index 0 with the string "Eddy"

# 1.Append method: Adds an element at the end of the list, therefore takes no arguments.
list.append("Samuel")
print(list)
list.append("Alinda")
print(list)

# 2.Remove: Removes the given element from the list, it takes exactly one argument.
list.remove("emma")
print(f"\nThe lis after removing emma is: {list}\n")
    #rremoving an element using del
del list[1]
print(f"\nThe lis after removing dani is: {list}\n")

# 3.Pop: Removes the given element at an index provided, it takes exactly one argument(index).
list.pop(0)
print(list)

# 4.Insert: Add elements to the list at the index provided, it takes exactly two argument(index and the element).
list.insert(0, "Karen")
list.insert(1, "Jordan")
list.insert(2, "Roy")
print(list)

# 5.Sort: Removes the given element from the list, it takes exactly one argument.
list.sort() # from low to high, asscending to descending.
print(list)
list.sort(reverse=True) # from high to low, descending to asscending.
print(list)

# 6.Index: returens the index of a given element in the list.
print(list.index("Samuel"))
print(list.index("Karen"))
print(list.index("Alinda"))

# 7.Count: counts the number of times a value appears in a list.
print(list.count("Karen"))
print(list.count("Samuel"))

# 8.Extend: This method extends a list by appending items. The benefit of this is you can add lists together.
list2 =["sam", "henry", "linus"]
list2.extend(list)
print(list2)

# Slicing a list
print(list2[:3]) # prints elements of the list up to index 3-1
print(list2[::3]) # prints the values of the list every after 2 elements(3-1).
print(list2[::2]) # prints the values of the list every after 1 element(2-1)