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