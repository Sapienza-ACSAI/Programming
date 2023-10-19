# Programming Unit 2

# --------------------- Lesson 7 ---------------------

# If in an "if" statement we put two strings,
# Python will return True if the alphabetical order is respected

print("a" > "b")  # False because a comes before b

print("a" < "b")  # True because a comes before b

print("A" < "a")  # True because capital A comes before lower-case a

print("B" < "a")  # True because capital A comes before lower-case B

# The order is:
# 1) Capitals;
# 2) Lower-case.

# In strings some sequence of characters have different properties:
# - \n: makes a new line;
# - \t: makes a tab;

# In the ASCII (ASCII is a subset of Unicode) table, the first 20
# characters are special characters. Every character has a code,
# and with the chr() function we can get either a character if the
# input is a code; with ord() we get a code if the input is a character

print(chr(12137))

print(ord("k"))

# In Python lists are a powerful tool that allow us to operate faster
# on items. By having a string and passing it with the split(separator) function,
# Python will return us a list of elements, based on what we decided that
# the separator was

mySentence = "I saw Nand doing bad stuff with the sea otters..."

myNewList = mySentence.split()

print(myNewList)

print(myNewList[2:4])

# Lists can contain different sort of values

myFantasticList = [1, 2, 5423.432, True, "else", None]

print(myFantasticList)

# Lists can be summed or subtracted (subtraction works as long as the items in the
# list that we are subtracting are present in the first list). We can even
# multiply a list by an integer

print(myNewList + myFantasticList)

print(myFantasticList * 2)

# If we want to add to a list a value from another list we have to do like that

print(myFantasticList + [myNewList[-1]])

# myNewList has to be treated as a new list

# With array.append(x) the element x is inserted in the last position of the array
# With array.insert(x, y) the element x is inserted in the array in position y

# Using the dir() function and inserting the type of class as input, it will
# return all the possible methods for that class

myEpicNewUnprecedentedListOfWonderOhMyGodItsBeautiful = [4, 4, 23, 42, 42, 42, 4, 2, 234, 234, 234, 1]

def double_int_list(inputList):
    outList = []
    for parappapperoZi in inputList:
        outList.append(parappapperoZi*2)
    return outList

print(double_int_list(myEpicNewUnprecedentedListOfWonderOhMyGodItsBeautiful))

def appendMyOdds(inputList):
    outList = []
    for elem in inputList:
        if elem % 2 != 0:
            outList.append(elem)
    return outList

print(appendMyOdds(myEpicNewUnprecedentedListOfWonderOhMyGodItsBeautiful))

def ifInBothLists(listOne, listTwo):
    commonList = []
    for elem in listOne:
        if elem in listTwo:
            commonList.append(elem)
    return commonList

print(ifInBothLists(myFantasticList, myEpicNewUnprecedentedListOfWonderOhMyGodItsBeautiful))

newList = [3, -312, 3, 32, 645, -53, -31, 645, -31298]

def setToZeroAllNegs(myList):
    for i in range(len(myList)):
        if myList[i] < 0:
            myList[i] = 0
    return myList

print(setToZeroAllNegs(newList))

def whatShouldIDo(myList):
    myOutput = True
    for i in range(len(myList)):
        if myList[i] >= myList[i + 1] and i+1 < len(myList):
            myOutput = True
        elif myList[i] < myList[i + 1]:
            myOutput = False
    return myOutput

print(whatShouldIDo([1, 4, 645, 6345, 53534, 534543543]))
