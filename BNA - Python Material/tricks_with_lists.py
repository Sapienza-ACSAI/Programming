# Define a function that gets a list of integers and returns a new list witthe same integers doubled

# el is a variable that the programmer defines

def double_int_list(a_list):
    new_l = [] # create new empty list
    for el in a_list: # for each element in the a_list
        new_l.append(2*el) # multiply the element by 2 and insert it in the new_l (adds it to the end)
    return new_l

# Define a function that gets a list of integers and returns a new list with only the odd elements of the original list

def only_odds(a_list):
    new_l = []
    for el in a_list:
        if el % 2 == 1: # if odd
            new_l.append(el)
    return new_l

# Define a function that gets two lists and returns a new list with all the elements that are in both the lists.

def list_intersection(list_a, list_b):
    new_l = []
    for el in list_a:
        if el in list_b: # if the element is also in b:
            new_l.append(el) # put it in the new empty list
    return new_l
        
'''
for i in range(5, 10) 

is kinda equivalent to saying

for i in a_list[5:10]

'''
# Define a function that gets a list of integers and returns a new list with only the elements greater than the average of the list.
        
def list_average(a_list):
    new_l = []
    a = sum(a_list) / len(a_list) # a = average = sum/number of items in said list
    for n in a_list:
        if n > a:
            new_l.append(n) # assign n to new list
    return new_l # print the numbers that are bigger than the average

# A function that gets a list of integers and sets all the elements of the lists that are negative to 0 

def zero_negative_values(a_list):
    for e in a_list:
        if e < 0: # if it's a negative integer
            e = 0 # set it to zero and overwrite the existing list
    return a_list

'''
The code above will NOT work because we cannot just replace an item of a list like that. e just gets the value of the element in a list, it just READS it and assigns itself that value.

(e) element is JUST a variable!!!

We only use the code above if we want to GET the values. 

'''
def correct_version_of_zero_negative_values(a_list):
    for index in range(len(a_list)):
        if a_list[index] < 0: # this actually goes INSIDE the list and IS the value itself
            a_list[index] = 0
    return a_list
    
''' We use the code above if we want to modify the elements'''

# Define a function that gets a list of integers and returns True only if the list is ordered in ascending order

def ascending_order(a_list):
    for e in range(len(a_list)):
        return a_list[index] < a_list[index-1]:
            
        
        LOOK AT THE LAST ONE
        
        
        
        
        
        
        
        
        