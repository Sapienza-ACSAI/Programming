# Programming Unit 1

# --------------------- Lesson 1 ---------------------

from math import floor, ceil
import random as rand
rand.seed()

# We can store variables

#          +0123456789AB
myString = "Parappappero"
#          -BA9876543210

myCake = "Since I like at the max of my capacities I feel good"

#  0   1   2   3   4   5   6   7   8   9   10  11
#  P   a   r   a   p   p   a   p   p   e   r   o
# -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   0

# With myString[x:y:z] we are specifying to return:
# -> all the characters in the position x:y with y excluded
# -> one character every z characters
#

print(len(myString))
print(len(myCake))

print("------------------------------------")

print("You asked for " + myString[3:7] + " and " + myString[10:12] + " without " + myString[0])
print("But what if I said " + myString[0:-9] + " or " + myString[2:11:4])
print("Ah, screw this, I'll give you " + myString[3:len(myString)-1:2] + " in exchange for " + myString[::2] + " or " + myString[::3])
print("Remember that the " + myCake[30:32] + myCake[10:12] + " is a lie")
print("However " + myCake[int(floor(len(myCake)/5)):int(ceil(len(myCake)/3)):2] + " was only a request by someone else")

print("------------------------------------")

# Print the number of "A"'s in the word

def howManyAs(word):
    counterMotherFucker = 0
    for c in word:
        if c.casefold() == "a":
            counterMotherFucker += 1
    return counterMotherFucker

print("The number of A's in the string '" + myCake + "' is " + str(howManyAs(myCake)))

print("------------------------------------")

nomiFighi = ["Oscar", "Elisabetta", "Leonardo", "Fernando", "Nil", "Gaia", "Francesco", "Giovanni", "Elena"]
ao = "əcitere ,everg " + nomiFighi[rand.randint(0, len(nomiFighi)-1)][::-1] + " oA"

print(ao[::-1])