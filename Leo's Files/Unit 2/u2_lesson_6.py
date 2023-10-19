# Programming Unit 2

# --------------------- Lesson 6 ---------------------

# Strings can be easily managed by Python. An example is
# the splicing of any string

myFirstString = "Hello World"

# With [x:y:z] we obtain different results. Every value has
# a different meaning:
# -> X: defines where Python should start to read the string;
# -> Y: defines where Python should end the reading of a string.
#       Y itself is not included in the subset;
# -> Z: defines the splicing of the string, so that Python
#       outputs a character each Z characters;

print(myFirstString[2:9:2])

# On https://docs.python.org/3/ are listed all the possible
# methods to treat a string.

# str.count(x) returns how many times the given character (x)
# is present inside the string

print(myFirstString.count("o"))

