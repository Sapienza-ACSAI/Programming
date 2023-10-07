
d = {(1, 2):6, (4, 5):9, (5, 6):10}

for key, value in d.items():
    print(f"The key {key} has value {value}")
    print('The key', key, 'has value', value)
    print('Tke key '+str(key)+' has value ' +str(value))
    print('They key {} has value {}'.format(key, value))    

d.pop((4, 5)) # will return the value related → 9

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''DICTIONARY COMPREHENSION'''

da = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
{k:v*2 for (k,v) in da.items()}
#  {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Write a function that takes a list of elements as input, and returns a dict where the keys are the elements of the list and the values are the number repetitions of that element in that list

def count_repetitions_mine(a_list):
    d= {}
    for i in a_list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

        '''PROF'S SOLN'''
        
        # def count_repetitions1(a_list):
        #     d = dict()
        #     for i in a_list:
        #         if i not in d:
        #             d[i] = a_list.count(i)
        #     return d
        
        # def count_repetitions2(a_list):
        #     d = dict()
        #     for i in a_list:
        #         d[i] = d.get(i, 0) + 1 # get 1, if not, 0
        #     return d
        
        # def count_repetitions3(a_list):
        #     d = {}
        #     while len(a_list) != 0:        # or a_list == []
        #         if el not in d:
        #             d[el] = a_list.count(el)
        #                 for i in range(d[el]):
        #                     a_list.remove(el)     a_list becomes an empty list
        #     return d

def count_repetitions_dictionary_comprehension(a_list):
    return {i:a_list.count(i) for i in a_list}

print(count_repetitions([1,1,1,2,3,4,1,1,'a','a','b',1.1]))
#output should be {1:5, 2:1, 3:1, 4:1, 'a':2, 'b':1, 1.1:1}



