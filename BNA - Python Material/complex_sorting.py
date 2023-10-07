# ------------------- Exercises for Friday 18/11 on Q2A

# Write the following function that could be used as a sorting key:
# To order a list of strings considering the number of vowels in increasing order, then the whole length in increasing order, then the reverse alphabetical order.

LS = ['apple', 'banana', 'clementine', 'pear', 'plume', 'avocado']

def myorder(string):
    return (-sum([1 for c in string if c in 'aeiou']), -len(string), string)

print(sorted(LS, key = myorder, reverse = True))

# To order a list of integers so that the odd numbers appear before the even numbers and the odd numbers are in increasing order, while the even numbers are in decreasing order.

ls = [6, 8, 3, 5, 1, 9, 7]

def myorder2(number):
    return -(number % 2), number if number%2 else -number

print(sorted(ls, key = myorder2, reverse = True))

# 6 → (0, -6)   result is [6, 8, 9, 7, 5, 3, 1]
# 8 → (0, -8)
# 3 → (-1, 3)  for 6 and 8 → zeros are equal so we skip to the next condition
# 5 → (-1, 5)
# 1 → (-1, 1)
# 9 → (-1, 9)
# 7 → (-1, 7) sorts according to these tuples
