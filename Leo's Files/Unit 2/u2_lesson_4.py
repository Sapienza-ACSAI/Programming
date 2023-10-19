# Programming Unit 2

# --------------------- Lesson 4 ---------------------

# When defining a function we can write a parameter directly
# inside the function's needed variables. If we must define
# a constant, we'll write it in capital letters. For
# example we could have PI = 3.14


def erone_sqrt(x, eps = 0.001):
    g = x/2
    print("The original G was " + str(g))
    numberOfApprox = 0
    while abs(g**2 - x)>eps:
        g = (g+x/g)/2
        numberOfApprox = numberOfApprox + 1
        print("- Approximation number " + str(numberOfApprox) +" of G was " + str(g))
    return g

erone_sqrt(5576543)