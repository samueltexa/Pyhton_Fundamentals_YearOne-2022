"""A dictionary is a kind of data structure that stores items in key-value pairs.
A key is a unique identifier for an item, and a value is the data associated with that key.
Dictionaries often store information such as words and definitions, but they can be used for
much more. Dictionaries are mutable in Python, which means they can be changed after they are created.
They are also unordered, indicating the items in a dictionary are not stored in any particular order."""

# Example1
# A sample dictionary variable
# Example2
Dictionary = {'food': 'Spam',
              'quantity': 4,
              'color': 'pink',
              4:"samuel",
              4:"Harry"}
#Duplicate values will overwrite existing values:
print(Dictionary)
print(Dictionary[4]) #print value having key=4

# Length of a dictionry
print(len(Dictionary))

"""Dictionary Items - Data Types
The values in dictionary items can be of any data type. There can be a list in a dictionary,
a dictionary in a dictionary"""
# alist with in a dictionary
dictionary = {'country': 'Uganda',
              'Region': "Mbarara",
              'Village': 'Kashanyarazi',
              "friends":["samuel","Marley","Allen"]}
print(dictionary)
print(type(dictionary))
# dictionary with in a dictionary
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
      'job': ['dev', 'mgr'],
      'age': 40.5}
rec['job'].append('web developer')
print(rec['name']['first'])
print(rec['name']['last'])
print(rec)

webstersDict = {(1, 2.0): 'tuples can be keys',
                1: 'ints can be keys',
                'run': 'strings can be keys'}
                #['sock', 1, 2.0]: 'lists can NOT be keys
print(webstersDict)

# The dictionary constructor
dictionary1 = dict(name="jack", age=21, color="Brown")
dictionary1['age']+=2
dictionary1['name']+='son'
print(dictionary1)
print(type(dictionary1))
# adding a new key-value pair to the dictionary
dictionary1['likes']=['skating','hiking','mountain climbing']
# updating a key value in the dictionary
dictionary1['age']=24
# removing a key from the dictionary
del dictionary1['name']
print(dictionary1)

"""Dictionary methods and ways of accessing the dictionary
dict.update(), dict.pop(), and dict.popitem()."""

# Update Method
"""The update method is very useful for updating multiple key values pairs at a time.
It takes a dictionary as an argument."""
# Using update method to add two key value pairs at once
dictionary1.update({'ran': 'running',
                     'shoes': 'slides'})
dictionary1.update({'age':25})
print(dictionary1)

# Pop method, works as the same as the del
"""The pop method removes a key and returns the value."""
dictionary1.pop('age')
print(dictionary1)

# Keys method: The keys method returns the keys in the dictionary.
print(dictionary1.keys())

# Values method: The values method returns the values in the dictionary.
print(dictionary1.values())

# Items method: he items method returns a list-like object of tuples in which
# each tuple is of the form (key, value).
print(dictionary1.items())

# Get method, returns the value of the key. It takes in a key as an argument. Returns none by default.
print(dictionary1.get('samuel'))
print(dictionary1.get('color'))

# iterating in a dictionary
for key in dictionary1:
    print(key)
    
for i in dictionary1.values():
    print(i)
    
for i in dictionary1.items():
    print(i)
    
for i in dictionary1.keys():
    print(i)
    
    
# converting a list, tupples, sets into a dictionary
"""Using dict"""
list=[('red',1),('blue',2),('green',3)]
converted=dict(list)
print (converted)#Output:{'red': 1, 'blue': 2, 'green': 3}

#converting two list into a dictionary using zip
list1 = [1,2,3,4]
list2 = ['sam','roger','zack']
joined= zip(list1,list2)
converter= dict(joined)
print(converter)

# copy method: Makes a copy of the dictionary
new = converter.copy()
print(new)

#Merging two dictionaries
dictionary1 = {"Name":"Kampala","Country":"Uganda"}
dictionary2 = {"Name1":"Alabama", "Country1":"America"}
merge = {**dictionary1, **dictionary2}
print(merge)