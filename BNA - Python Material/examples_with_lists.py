# Write a function that gets a list of ints and returns a new list with only the elements in an even position.

def even_in_list(evenlist):
    new_l = []
    for n in evenlist:
        if evenlist.index(n) % 2 == 0: # operations with position number of item
            new_l.append(n)
    return new_l

            '''PROF'S SOLN'''
            
            # def even_list(l):
            #     new_l = []
            #     for i in range(len(l)):
            #         if i % 2 == 0:
            #             new_l.append(l[i]) #l[i] is ELEMENT bc range deals with indexes
            #     return new_l
            
            # def even_list2(l):
            #     new_l = []
            #     for i in range(2, len(l), 2): # takes 2 steps, so each element is 
            #         new_l.append(l[i])
            #     return new_l    
            
            # def even_list3(l):
            #     return [l[i] for i in range(2, len(l), 2)]
            
            # def even_list4(l):
            #     return l[2::2] # starting from 2. skipping 2
            
            # def even_list5(l):
            #     return [item for index, item in enumerate(l) if index%2==0]
            
            '''PROF'S SOLN DONE'''

# Write a function that gets a list with any possible value types and returns a new list with only the integers of the list in input.

def type_of_list(l):
    new_l = []
    for i in l:
        if type(i) == int: # if it's an integer, append it to the list
            new_l.append(i)
    return new_l

            '''PROF'S SOLN'''
            
            # def only_int_list(l):
            #     new_l = []
            #     for i in range(len(l)):
            #         if type(l[i]) == int:
            #         # or you could use → if isinstance(l[i], int)
            #         new_l.append(l[i])
            #     return new_l
            
            # def only_int_list2(l):
            #     new_l = []
            #     for index, item in enumerate(l):
            #         if type(item) == int:
            #             new_l.append(item)
            #     return new_l
            
            # def only_int_list3(l):
            #     return [item for item in l if type(item) == int]
            #     # returns a list automatically since this is LIST compression
            
'''VERY IMPORTANT'''
            # def only_int_list4(l):
            #     return [item for index, item in enumerate(l) if index%2==0]
            
            '''PROF'S SOLN DONE'''
           
# Write a function that gets an int n and creates a list with all the integers from 0 to n. Starting from 2, it removes all multiples of the list elements. Returns the list with the remaining elements.

# T H I S D O E S N O T W O R K 
def create_list_with_n():
    n = int(input("Give me a number: "))
    zero_to_n = [0] # division by 0 doesnt work so list starts with 0 pre-installed
    for k in range(0, n+1):
        zero_to_n.append(k)
    print (zero_to_n)
    for i in range(1, n+1):
        if i % 2 == 0:
            zero_to_n.remove(i) # able to do this for 2, repeat for each element
    return zero_to_n


            '''PROF'S SOLN'''
            
            # def only_prime(n):
            #     l = list(range(2, n+1))
            #     for i in range(2, n):
            #         for j in range(2*i, n+1, i): # we start from 2, go until n+1
            #         (because we need n to be included), step by i
            #             if j in l:
            #                 l.remove(j) # remove the multiple of i from list
            #     return l
            
                
            # def only_prime2(n):
            #     l = list(range(2, n+1))
            #     for i in range(2, n):
            #         for j in range(2*i, n+1, i): # we start from 2, go until n+1 (because we need n to be included), step by i
            #             try:
            #                 l.remove(j)
            #             except ValueError:
            #                 pass
            #     return l
            
            '''PROF'S SOLN DONE'''         

# Write a function that gets two lists of ints and appends in the first list only the elements of the second list that are not already in the first list.

def two_lists_addition(list1, list2):
    ints_list = list1 + list2
    temp = []
    for x in ints_list:
        if x not in temp: # if an item is NOT in temp, it puts it in temp and when it comes back to the same element it doesn't repeat
            temp.append(x)   
    ints_list = temp
    print(temp)

# Write a function that gets two lists of integers. It inserts new elements in the first list, considering the elements of the second list as positions in the first list and the indexes of the elements as the values to be inserted (i.e., if the second list is [4, 2, 3] it inserts 0 in position 4, 1 in position 2 and 2 in position 3). If a position is outside the first list, the value is ignored.

def list_mishmash(list1, list2):
    for i in list2:
        list1.insert(int(i),list2.index(i))
    return list1
  

#####################################################
# EXTRA WRONG ONE #
# A function that takes number k as an input and removes the multiples of k from a list that has numbers from 0 to k.
'''
def create_list_with_n():
    n = int(input("Give me a number: "))
    zero_to_n = [0] # division by 0 doesnt work so list starts with 0 pre-installed
    for k in range(1, n+1):
        if n % k != 0:
            zero_to_n.append(k)
    return zero_to_n
'''
print(even_in_list([2,3,8,7,1,4,5,9])) #[2, 8, 1, 5]
print(type_of_list([1, "hello", 3, 4.0, 5])) #[1, 3, 5]
print(create_list_with_n()) # didnt finish
print(two_lists_addition([1, 3, 4, 5], [1, 2, 4, "a"])) #[1, 3, 4, 5, 2, 'a']
print(list_mishmash([1, 2, 3, 4, 5, 6], [4, 2, 3])) #[1, 2, 1, 2, 3, 4, 0, 5, 6]
