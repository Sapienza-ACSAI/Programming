# Write a function that gets two int numbers (a and b) as input
# returns the sum of all odd numbers within the range (a and b included).

'''PROF'S SOLN'''
    
def odds_sum(a, b): 
    
    if a > b:
        a, b = b, a # makes a the smaller number of the range at all times
    
    total = 0 # we start with the sum at 0
    
    #assuming that a < b and x is a < x < b
    if a % 2 == 0:
        x = a + 1 # we start the count by setting x as an odd number
    else:
        x = a # if x is not even it starts from a
    while x <= b: # and while x is inbetweeen a and b,
        total += x # we add x to the total
        x += 2 # adding 2 to x always makes it the next odd number.
    return total

print(odds_sum(10, 20)) # use print if the function ends with return

#----------------------------------------------------------------------------

# Write a function that gets an int number (n) as an input and prints
# all the ints smaller or equal to n that are perfect squares
# (x is a perfect square if it exists an int y so that x==y*y).
# The function returns the highest number printed.

'''PROF'S SOLN'''

def perfect_squares(n):
    x = 1
    while x*x <= n: # the loop will break if x squared goes over n
        print(x*x) # will always print perfect squares
        x += 1
    return (x-1)*(x-1) # returns the highest number printed since the
    #loop stops at an x value that when squared, passes n

# here is a test number
perfect_squares(100)

''' MY SOLUTION

from math import sqrt

def perfectsquarefinder():
    n = int(input("Give me a number: "))
    while True:
        if sqrt(n) == int(sqrt(n)):
            print (n)
        n -= 1
    
print (perfectsquarefinder())

'''
#----------------------------------------------------------------------------

# Write a function that gets an int number (n) as an input
# and prints all its factors.
# The function returns the number of factors printed.
# For example, if n is 150, the function will print
# 2
# 3
# 5
# 5

def factorize(n):
    
    if n < 0 or type(n) != int: # if n is negative or not an integer
        # isinstance (n, (int, float)) 
        # isinstance can check for multiple types at once
        raise ValueError('Cannot factorize')
        # if the input doesnt match the assumptions of the code,
        # we use raise ValueError to let the user know that the
        # input is unexpected.
    counter = 0
    x = 2 # x is the first prime number besides one, we start with x
    while x <= n:
        if n % x == 0: # if n is divisible by x
            print (x)
            n = n // x # n would become → n integer division x 
            # because we need integers and not floats, normal
            # division gives you floats (ex: 2.0)
            counter += 1 # number of factors
        else:
            x += 1
    return counter
#----------------------------------------------------------------------------
 
# Write a function that gets an int number (n) as an input and prints
# all the integers smaller or equal to n that are powers of 2.
# The function returns the highest number printed.

'''PROF'S SOLN'''

def powers_of_two(n):
    x = 0
    while 2**x <= n:
        print (2**x)
        x += 1
    return 2**(x-1)

powers_of_two(30)
powers_of_two(128)
    

''' MY SOLUTION
import math

# Function to check
# Log base 2
def Log2(n):
    return (math.log10(n) / math.log10(2));

def poweroftwofinder():
    n = int(input("Give me a number: "))
    while True:
        if (math.ceil(Log2(n)) == math.floor(Log2(n))): # if the rounded up
        #version is equal to the rounded down version, it should be a power of 2
            print (n)
        n -= 1
      
    while True:
        if (math.ceil(Log2(n)) == math.floor(Log2(n))): # if the rounded up
        #version is equal to the rounded down version, it should be a power of 2
            print ("The highest power of 2 is:", n)
            break
        else:
            n -= 1
    
print (poweroftwofinder())
'''
     
        
        
            

