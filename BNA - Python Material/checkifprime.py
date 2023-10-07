# tast: check if a number is prime

def is_prime(x): # return True if x is prime, False otherwise
    K = 2 # if it's a constant it's usually written in capital letters
    while K != x//2 and x % K != 0: # while K is not equal to half of x
        K += 1 # assign K a new value by adding 1
    if K == x//2: # integer divison
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(is_prime(4569854526))
    print(is_prime(97))
    print(is_prime(2))
    print(is_prime(0))
       
# when you execute (is_prime) you dont expect an output
# when we say "print" we are expecting an output
    
# --------------------

# the prof's solution !!!
def is_prime(x): # return True if x is prime, False otherwise
    K = 2 
    while x % K != 0 and K < x:
        K = K + 1
    if K == x:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(is_prime(4569854526))
    print(is_prime(97))
    print(is_prime(2))
    print(is_prime(0))
       






    
    