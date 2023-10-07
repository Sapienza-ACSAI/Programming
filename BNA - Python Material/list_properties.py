
'''IMPORTANT NOTE!'''

def change(A):
    A = 10

x = 5
change(x)
print(x) # this will return 5 because what happens inside the function stays inside the function

def change(A):
    A[0] = 10

x = [5, 6, 7]
change(x)
print(x) # but for this, we get [10, 6, 7]

'''Remember that lists are stored inside the memory!'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

list1.remove(element) # this function removes the first occurence of the element
# you have to be sure that the element is in the list if you want to use "remove"

list1.pop(index) # this takes in an INDEX and outputs the element at that position
'''ex: list=[0, 1, 2, 3] → list.pop(0) → 0'''

del list1[index] # deletes the item at given index

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

a_list = [5, 7, 0, 29, 100]

b_list = a_list[:]
# assigns all elements in a to b → creating a duplicate of a

c_list = a_list.copy()
# this is not deepcopy!!!
# copies all items in a to c → creating a duplicate of a

d_list = list(a_list)
# lists all items in a → creating a duplicate of a

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

a_list = [50, 7, 0, 29, 100]
a_list.sort() # sorts in ascending (increasing) order
# a_list is now [0, 7, 29, 50, 100], the list was MODIFIED

a_list = [50, 7, 0, 29, 100]
a_list.sort(reverse = True) # MODIFIES a_list to be modified in descending (decreasing) order


a_list = [50, 7, 0, 29, 100]
sorted(a_list) # sorted but DOESNT MODIFY the a_list

l = ['asd', 'a', 'zxcv', 'qwerty']
print(sorted(l, key = len))# sorts according to length, DOESNT MODIFY the list
# ['a', 'asd', 'zxcv', 'qwerty']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

(3, 4, 5) < (1, 4, 5) # compares item by item
# False
('asd', 1000, 5) > ('asd', 4, 6)
# True since 1000 > 4, the checking stops when conditions are met

x=4
def foo(x):
    print("In foo, x is", x) # x is 4
    x = 5
    print("In foo now, x =", x) # x is 5

foo(x)
print(x) # will print 4 because x is only changed in the foo function

def myfunction(l):
    if len(l) > 0:
        l[0] = 50 #overwrites existing value
    return l

myfunction(a_list)
print(a_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 





      