# Write a function that gets a string as an input, prints a message describing the type of string received and returns the length of the string. It should distinguish if:
# it only contains letters
# it only contains lower-case letters
# it only contains upper-case letters
# it only contains numerical digits
# it only contains letters and digits
# it starts with a lower-case letter
# it ends with a dot ('.')

def define_string():
    x = input("Please input a string for analyzation: ")
    
    if x.isalpha():
        print ("This string only contains letters.")
    if x.islower():
        print ("This string is only composed of lower-case letters")
    if x.isupper():
        print ("This string is only composed of upper-case letters")
    if x.isnumeric():
        print ("This string is only composed of numerical digits")
    if 

#  define_string()

#----------------------------------------------
# Write a function that gets two strings (a and b) as input and returns the string resulting from joining the shorter and the longer.

def join_short_long():
    a = (input("Please input string A: "))
    b = (input("Please input string B: "))    
    result = None
    if len(a) > len(b): # if we don't do len() and the string contains numbers, it will print the numbers that are small first
        result = b + a
    else:
        result = a + b
    return result

print(join_short_long())

'''MY SOLUTION
def add_two_strings():
    a = (input("Please input string A: "))
    b = (input("Please input string B: "))
    if len(a) > len(b): 
        print(b,a)
    else:
        print(a,b)
        
add_two_strings()
'''
#--------------------------------
b = "Hello world"
b
b[0]
b[1]
b[0:5]
b[:4]
b[4:]
x = input("Tell me a number: ")
type(x)
x = int(x)
x
x = 67
x
x = "5 6 8 0"
int(x(0))
int[x(0)]
int(x[0])
int(x[0]) + int(x[-1])
int(x[0]) + int(x[11])
int(x[0]) + int(x[4])
x = "56789"
int(x[0:2]) + int(x[2:])
int(x[0:2]) + int(x[3:])
len(x)
len(b)
str.upper(b)
str.lower(b)
str.upper(x)
str.lower(x)
b.upper()
str.upper(x,b)
b.capitalize()
b.count()
b
a.count("o")
b.count('o')
help (b.count)
a.isalpha()
b.isalpha()
b[:-1].isalpha()
b[:-5].isalpha()
b[:-6].isalpha()

# assume that b is a 21 character string
b[20:0:-1] # prints all in reverse order
b[::-1] # also prints all in reverse order
%history -f intro_to_strings.py

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sentence = "today is a very beautiful day!"
print(sentence.split()) # THIS PRINTS
['today', 'is', 'a', 'very', 'beautiful', 'day!']

len(sentence.split()) # how many strings did it split to
6

for element in list_of_integers:
    print(element)
    # PRINTS ALL ELEMENTS OF THE STRING ONE BY ONE
    













