# Programming Unit 2

# --------------------- Lesson 8 ---------------------

# There are various methods to copy lists. One way is to
# use the copy() method

listOne = [423, 12, 43, 423, 4, 423, 4, 2, 4, 4, 234, 24, 23, 543, 534, 5]

listTwo = [6, 456, 543, 76, 7, 568, 78, 768, 765, 74, 45, 35, 756, 6, 76]

# Clearly listOne and listTwo are different. Let's copy listOne
# in another variable

listThree = listTwo.copy()

# listThree will be a copy of listTwo, but it will be independent
# from the original

print("List One:", listOne)
print("List Two:", listTwo)
print("List Three:", listThree)

# We can try to edit listThree, and it will remain independent:

listThree[-1] = 83754

print("List Two:", listTwo)
print("List Three:", listThree)

# In a list of lists we can concatenate more indexes

listOfLists = [[2, 43, 423, 654, 876], [345, 534, 74, 2345, 6, 234, 62, 35, 423], [312, 312, 5, 45, 353, 4], [42, 423, 42, 3, 645, [6456456, 45, 6457, 756, 234, 132], 634, 645, 645, 243]]

print("List of lists with index [3][5]:", listOfLists[3][5])
print("List of lists with index [3][5][4]:", listOfLists[3][5][4])

# We can even edit an item of those lists using multiple indexes

listOfLists[3][5][4] = 423131

print("List of lists with index [3][5][4] edited:", listOfLists[3][5][4])
print("List of lists with index [3][5] edited:", listOfLists[3][5])

# To sort a list we have two ways:
#  - Using <list>.sort(): IT MUSTN'T BE STORED IN A VARIABLE, IT WILL RETURN NONE;
#  - Using sorted(<list>, <optArgs>)

sortedListOne = sorted(listOfLists[3][5], reverse=True)

sortedListTwo = listOfLists[3][5]
sortedListTwo.sort(reverse=True)

print("Here are the two lists sorted:", sortedListOne, "and", sortedListTwo)

# To compare two lists we can use the operators <, <=, >, >=

print("Is list[3][5] smaller than list[2]? Python says", listOfLists[3][5] < listOfLists[2])

sortedListOneByLength = sorted(listOfLists, key=len)

print(sortedListOneByLength)