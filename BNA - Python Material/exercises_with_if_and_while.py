
# assuming that we dont have access to calcullating the sqrt, this function
# is made to approximate the sqrt

def erone_sqrt(x, epsilon =0.001): # we're trying to approximate the sqrt of x
    g = x/2  # guesses the interval and starts checking halfway points
    print(g)
    while abs(g**2 -x) > epsilon: # how different is g from x?
        g = (g + x/g)/2 # updates the g value to be closer to sqrt of x
        print (g)
    return g # if g^2 is close enough to x, show g to user and finish the job

# call function from console such as     erone_sqrt(324324)



# Write a function that asks the user for three grades as input (using the input function)
# and returns the average of the grades only if all the grades are legitimate
# (i.e. 0<=grade<=30), returns False otherwise


def grades():
    grade_a = float(input("Please input first exam grade: "))
    grade_b = float(input("Please input second exam grade: "))
    grade_c = float(input("Please input third exam grade: "))
    
    if 0<=grade_a<=30 and 0<=grade_b<=30 and 0<=grade_c<=30:
        # if all values are valid, return calculated average
        return (grade_a + grade_b + grade_c)/3
    else:
        # one of the values is invalid → False
        return False
    
if __name__ == "__main__":
    print(grades())
    
    
# Write a function that gets a float number as an input, 
# calculates its cube root, prints on screen, and returns it
def cube_root():
    number = float(input("Please input a number: "))
    number = number ** (1/3)
    print (number)
    return

if __name__ == "__main__":
# if name of the file is main run the file
    cube_root()


# Write a function that gets three floats a, b, c, as an input
# and calculates and prints the two x roots of the equation and returns the
# greatest of the two

def roots():
    a = float(input("Please input first coefficient: ")) # we ask for the 
    b = float(input("Please input second coefficient: ")) # coefficients one by one
    c = float(input("Please input third coefficient: "))
    
    delta = b**2 - 4*a*c
    if delta == 0:
        print (-b/2*a) #if delta is 0 there is only one root so we print that
    elif delta < 0:
        print ("No real solution") #if delta is negative there is no real solution
    elif delta > 0:
        print(((-b) + (delta ** (1 / 2))) / 2 * a) #remember the quadratic formula
        print(((-b) - (delta ** (1 / 2))) / 2 * a) # we print x1 and x2
        return ((-b) + (delta ** (1 / 2))) / 2 * a # we return the bigger x
    
if __name__ == "__main__":
# if name of the file is main run the file
    roots()  



# Write a function that gets three integers as an input d, m, y
# (it is assumed that a is always an odd number to avoid leap years)
# and returns True or False depending on whether the three numbers
# form a valid date in the "d/m/y" format.
# Ex: 30/2/2017 False, 1/1/1111 True

def dateproblem():
    day = float(input("Please input day: "))
    month = float(input("Please input month: "))
    year = float(input("Please input year: "))
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 0<= day <= 31:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 0<= day <= 30:
            return True
        else:
            return False
    elif month == 2:
        if 0<= day <= 28:
            return True
        else:
            return False
    else:
        return False
    
    
if __name__ == "__main__":
    print(dateproblem())
    
    
# Write a function that gets five integers as an input and returns
# the sum of all even numbers minus the sum of all odd numbers

def evenandoddset(): #define a set of 5 numbers
    a = float(input("Please input number a: ")) 
    b = float(input("Please input number b: ")) 
    c = float(input("Please input number c: "))
    d = float(input("Please input number d: ")) 
    e = float(input("Please input number e: "))

    n = 0 #we define n as the starting point, we'll + or - in reference to n
    if a % 2:
        n -= a  #we check if a is even, if it is we subtract it from the total
    else:
        n += a # if not, we add it to the total
    if b % 2:
        n -= b # we repeat the same process for all the numbers
    else:
        n += b
    if c % 2:
        n -= c
    else:
        n += c
    if d % 2:
        n -= d
    else:
        n += d
    if e % 2:
        n -= e
    else:
        n += e
    return n


            
if __name__ == "__main__":
# if name of the file is main run the file
    print (evenandoddset()) # in the other excercises we printed the values in the
    # function however in this exercise we want to see the result we need to print
    # the function itself
    

