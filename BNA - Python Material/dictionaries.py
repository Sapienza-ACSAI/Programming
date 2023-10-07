""" DICTIONARIES """

# Dictionaries have a key and a value → both of them makes an item
# A dictionary is not ordered, you cannot use indexes

# The key is any constant object, they are UNIQUE so you cant have 2 of the same 
# Ex: cannot be a list but can be a TUPLE, can be a string, can be an integer
#     ↑           ↑
D  = {1: 'first', 2: 'second'}
#          ↑            ↑
# The value can be anything you can possibly imagine, they are/nt unique

for key in D:
    print(key, D[key]) # will print 1 first, 2 second

for key in D:
    print(key * 10) # will print 10, 20   

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
# A dictionary of temperatures
temps = {"Rome": [20, 21, 29], "Paris": [5, 10, 8]}

temps["Rome"].append(20) # adds 20 degrees to Rome's 4th day
print(temps)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# You can create a dictionary from a list of tuples
l = [('a', 2), ('b', 6), ('c', 4)]
dict(l) # out: {'a': 2, 'b': 6, 'c': 4}

var = 'a'
var in dict(l) # true bc it went through keys and found the key 'a'

2 in dict(l).values() # true bc 2 is a VALUE in dict(l)
dict(l).items() #out: dict_items([('a', 2), ('b', 6), ('c', 4)])


