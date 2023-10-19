# Programming Unit 2

# --------------------- Lesson 3 ---------------------

# Comments: there are two ways to write comments on Python:
# - With the "#" sign in the beginning of the line;
# - With """ after and before the area we want to consider as a comment

# How to define our custom function:
from math import pi

valueA = 24
valueB = 13

def cirlceMeasures(radius):
    def area(radius):
        return pi * radius ** 2

    def perimeter(radius):
        diameter = radius * 2
        return diameter * 2

    resultOfTheOperation = "The area of your circle is " + str(area(radius)) + ", while your perimeter is " + str(perimeter(radius))
    return resultOfTheOperation

print(cirlceMeasures(valueA))

def rectangleMeasures(base, height):
    def area(base, height):
        return base * height

    def perimeter(base, height):
        return base * 2 + height * 2

    resultOfTheOperation = "The area of your rectangle is " + str(area(base, height)) + " while your perimeter is " + str(perimeter(base, height))
    return resultOfTheOperation

print(rectangleMeasures(valueA, valueB))

print("------------")

students = int(input("How many students are in the group?"))
fullPrice = 5

def museum_cost(people, ticket):
    if people >= 20:
        singlePrice = (ticket / 100) * 80
        priceInt = singlePrice * people
        price = "The price with the discount of 20% is " + str(priceInt) + "€ because there are " + str(people) + " students"
        return price
    else:
        priceInt = ticket * people
        price = "The price without the students discount is " + str(priceInt) + "€ since there are " + str(people) + " students and you need at least 20"
        return price

print(museum_cost(students, fullPrice))

# We can even raise errors

valueX = input("Insert the 1st number")
valueY = input("Insert the 2nd number")
valueZ = input("Insert the 3rd number")

"""def threeNumberSort(valueX, valueY, valueZ):
    isXEven = True
    isYEven = True
    isZEven = True

    if isinstance(valueX/2) == False:
        isXEven = False

    if isinstance(valueY/2) == False:
        isYEven = False

    if isinstance(valueZ/2) == False:
        isZEven = False

    if isXEven == True and isYEven == True and isZEven == True:
        lowestNumber = min(valueX, valueY, valueZ)
        return lowestNumber
    elif isXEven == False and isYEven == False and isZEven == False:
        highestNumber = max(valueX, valueY, valueZ)
        return highestNumber

print(threeNumberSort(x, y ,z))"""

def three_numbers(x, y, z):
    answer = min(x, y, z)
    if x%2 != 0:
        answer = x
    if y%2 != 0 and y > answer:
        answer = y
    if z%2 != 0 and z > answer:
        answer = z
    return answer

print(three_numbers(valueX, valueY, valueZ))

# A Nesting Function is a function inside another function.
# The function nested inside the other function is executed
# first, like in maths. An example is the following:

myNestingFunction = int(input("Here is my example. But what about your input?"))
