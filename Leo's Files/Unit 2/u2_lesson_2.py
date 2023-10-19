# Programming Unit 2

from math import sqrt

# --------------------- Lesson 2 ---------------------
print(2)  # <-- It prints what it's inside the brackets

# We can use much of the signs to do most of the operations
# We can also use the inequalities signs

print(5 > 6)  # It will return "false", a boolean value

print(5 < 6)  # It will return "true", a boolean value

# There are multiple classes of values, such as:
# - Integers;
# - Float numbers;
# - Booleans;
# - Strings;
# - NoneType

# We can use the type() function to detect what type of value we are using

print(type(5 + 6))

print(type(7 / 8))

print(type(5 > 6))

print(type("Hello World! I love Sara"))

print(type(None))

# We can also use variables. To store a value inside a variable we must first define a name of the variable
# and then we must have a value to store inside the variable. We can store in the variable:
# - Numbers such as integers or float numbers;
# - Strings;
# - Functions

variable1 = 100

variable2 = "Hello World"

variable3 = variable1 + sqrt(variable1)

# Variable's name can't start with a number.
# Variables can be used inside functions such as print()

print(variable2)

print(type(variable2))

# if statements can be used to define a set of instructions and conditions. Here is an example

firstNumber = 200
if firstNumber > 199:   # if condition:
    myOutput = firstNumber + 1   # instructions to execute if the condition is true
else:   # else (so if the conditions isn't true)
    myOutput = firstNumber - 100   # instructions to execute if the principal conditions is false

print(myOutput)

# It executes the first set of instructions if 200 is greater than 199, otherwise
# it will execute the second set of instructions
