
'''THIS DOCUMENT CONTAINS INTRODUCTION TO SETS AND THE RANDOM LIBRARY'''

'''THERE IS A HINT AT THE END REGARDING HOMEWORK 4'''

'''EXERCISE:'''
# Write a function that takes a list of elements as input and a filename. It saves the input name of each element in the list and the repetition time with the "tab" character. The order in which each element appears in the file is the same of the list

def save_repetitions(array, filename):
    d = {}
    for i in array:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    with open(filename, 'w') as opened:
        for key, value in d.items():
            # opened.write((str(key) + '\t' + str(value)+ '\n'))
            print(key, value, sep='\t', file= opened)
    
save_repetitions([1, 1, 1, 7, 7, 3, 3, 3.4, 3.4, 3.5, 'house', 'a', 'a', 1], "saverepetitionstext.txt")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from random import randint
randint(-100, 100)

l = [randint(-100, 100) for i in range(5)] # creates a 5 element list of random ints
print(l)

# random.seed(0) '''LOOK INTO THIS!!'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# A and B are sets (just like in math)

A = {5, 6, 7, 8}
B = {6, 7, 8, 9}
print (A.union(B)) # {5, 6, 7, 8, 9}
print (A.intersection(B)) # {8, 6, 7}
print (A.difference(B)) # {5}

l = [randint(-100, 100) for i in range(5)]
s = set(l) # creates a set from a list

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

trial = ['apple', 'pineapple', 'orange', 'pear', 'peach']
sorted(trial)
sorted(trial, key = len) # sorted by length

trial_1 = [( (randint(-10, 10)), (randint(-10, 10)) ) for i in range(5)]
sorted(trial_1, reverse=True) # a list of tuples is sorted, reversed


def mykey(t):
    return t[::-1]

sorted(trial_1, key = mykey)

# - - - - - - - - -

'''HINT ON THE HOMEWORK'''

""[8:10] → # gives empty string
# it works only if you slice it 

[1, 2, 3, 4, 5][8:10] → # gives empty list

# THESE DO NOT CAUSE ERRORS

