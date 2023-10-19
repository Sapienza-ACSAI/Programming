# Programming Unit 2

# --------------------- Lesson 5 ---------------------

print("-------------Function 1-------------")

numberToVerify = int(input("Insert here the number you want to find out if it's prime: "))

def isPrimeNumber(number):
    k = 2
    h = number//2
    while number % k != 0 and k < h:
        k += 1
    if k == h:
        return "The number " + str(number) + " is a prime number"
    else:
        return "The number " + str(number) + " is not a prime number"

print(isPrimeNumber(numberToVerify))

# Problem: write a function that asks the user for integers
# until the user inserts 0. It returns the average of the inserted values

print("-------------Function 2 | Version 1-------------")

def averageUntilZero():
    userInput = int(input("Insert a number: "))
    numberOfInputs = 0
    sumOfInputs = 0
    while userInput != 0:
        sumOfInputs += userInput
        numberOfInputs += 1
        userInput = int(input("Insert a number: "))
    if userInput == 0 and numberOfInputs == 0 and sumOfInputs == 0:
        return "The average is 0"
    else:
        return "The average of the " + str(numberOfInputs) + " inputs is " + str(sumOfInputs / numberOfInputs)

print(averageUntilZero())

print("-------------Function 2 | Version 2-------------")

def auzSecondVersion():
    numberOfInputs = 0
    sumOfInputs = 0
    while True:
        userInput = int(input("Insert a number: "))
        if userInput == 0:
            break
        else:
            sumOfInputs += userInput
            numberOfInputs += 1
    if userInput == 0 and numberOfInputs == 0 and sumOfInputs == 0:
        return "The average is 0"
    else:
        return "The average of the " + str(numberOfInputs) + " inputs is " + str(sumOfInputs / numberOfInputs)

print(auzSecondVersion())

print("-------------Function 3-------------")

def negativeNumbers():
    negativeSum = 0
    while True:
        userInput = int(input("Insert a number: "))
        if userInput == 0:
            break
        elif userInput < 0:
            negativeSum += userInput
    if userInput == 0:
        return "You haven't inserted any numbers different from 0"
    else:
        return "The sum of all negative numbers is " + negativeSum

print(negativeNumbers())
