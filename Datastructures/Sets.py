"""A Set in Python programming is an unordered collection data type that is iterable,
mutable and has no duplicate elements. Sets are represented by { } (values enclosed in curly braces)"""
# Time Complexity: O(1)
# Auxiliary Space: O(1)

# Creating a set
myset = {'samuel','jack','ronald'}
print(myset)
print(type(myset))

# defining an empty set
emptyset = set()
print(type(emptyset))
print(emptyset)

"""<============PYTHON METHODS AND OPERATIONS=============>"""
# add()	Adds an element to the set. This takes exactly one argument
myset2 = {'jack','samuel','henry','hilary','innocent','jordan',30,10,11,90}
myset2.add('joseph')
myset2.add('chali')
print("myset2 with added elements:",myset2)

# copy() Returns a copy of the set
newset = myset2.copy()
newset.add('hero')
newset.add('joan')
print("new set with added elements:",newset)

# remove() Removes the specified element. it takes exactly one argument. Throws an error.
newset.remove('jack')
print("new set without jack:",newset)

# discard()	Remove the specified item.method will raise an error if the
# specified item does not exist, and the discard() method will not.
newset.discard('hilary')
print("new set new set without hilary:",newset)

# difference()	Returns a set containing the difference between two or more sets
difference1 = myset2.difference(newset)
difference2 = newset.difference(myset2)
print("differnce1 is:",difference1)
print("difference2 is:",difference2)

# difference_update()	Removes the items in this set that are also included in another, specified set
#The difference_update() method removes the items that exist in both sets.
myset2.difference_update(newset)
print(newset)

# pop()	Removes a random item from the set
print(myset)
myset.pop()
print(myset)

# update() The update() method updates the current set,
# by adding items from another set (or any other iterable).
myset.update(myset2)
print(myset2)

# clear()	Removes all the elements from the set
myset.clear()
print(myset)


"""Example2"""
set1 = {'jack','samuel','dog','hilary','innocent','jordan','racook',20}
set2 = {'cow','chiken',20,'dog','goat','sheep','rabbit','racoon','samuel'}

# intersection() Returns a set, that is the intersection of two or more sets
print("Intersection is:",set1.intersection(set2))

# union()	Return a set containing the union of sets
print("the union is:",set1.union(set2))

# isdisjoint() Returns whether two sets have a intersection or not
print(set2.isdisjoint(set1))

# issubset()	Returns whether another set contains this set or not
print(set2.issubset(set1))

# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
print("Intersection_Update is:",set2.intersection_update(set1))

# issuperset()	Returns whether this set contains another set or not
print(set2.issuperset(set1))

