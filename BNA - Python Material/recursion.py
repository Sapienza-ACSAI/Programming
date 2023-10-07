
"""RECURSION"""

# recursion allows us to call a function inside of itself, creating a loop repeating the amount of times the function repeats

# the factorial in math is a good example of this:
    # n! = n * (n - 1)!
    # 4! = 4*3! = 4*3*2! = 4*3*2*1! = 4*3*2*1*0! = 24
    # it calls n-1 recursively

def factorial(x):
    
  if x == 0:
    return 1
  else:
    return x * factorial(x - 1)

print(factorial(4))

# We can also use this concept to code a recursive palindrome detector

def palindrome(s: str) -> bool:
    
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    return False
    
print(palindrome("potatoes")) # False
print(palindrome("tattarrattat")) # True
print(palindrome("able was I ere I saw elba")) # True