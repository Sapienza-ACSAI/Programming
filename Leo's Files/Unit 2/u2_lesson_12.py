# Programming Unit 2

# --------------------- Lesson 12 ---------------------

# Considering the following items:

a, b, c, d, e = "apple", "banana", 5, 5.8, "excellence"

# To print all of them we use the print() function with multiple inputs

print(a, b, c, d, e)

# The elements will be printed, one by one, with each character followed by a space.
# For lists it's different though:

M = [[1, 2, 3], [100, 100, 100], [6.89, 9, 100]]

# If we use print(M) the output will be:
# >>> [[1, 2, 3], [100, 100, 100], [6.89, 9, 100]]
# However, there is a way to print the matrix, line by line, without using the
# for loop. We use print(*NameOfTheElement):

print(*M)

# This will output:
# >>> [1, 2, 3] [100, 100, 100] [6.89, 9, 100]
# We can even use a separator

print(*M, sep="\n")

# This way every row of the matrix will be printed in a new line. But what if we want to
# make so that each element of the matrix uses a defined X number of characters? We do it with padding:

myFormat = "{:6}"*len(M[0])

# {:X}
#  -> The : says that what's inside the curly brackets is a formatted string;
#  -> The X says how many characters each entry should have.
#
# We can use then the for loop to print each row, following out format

for row in M:
    print(myFormat.format(*row))

# We can even use the formats to print some numbers up to a certain point. For example:

decimalNumber = 85476.634671546534523542354235867

print("{:012.4f}".format(decimalNumber))

# {:X.Yf}
#  -> X stays for how many characters at least must be printed. If the number is shorter than X
#     then Python will add (X-lengthOfNumber) zeroes at the left of the number;
#  -> Y stays for how many decimal characters must be shown.

print("\n")

def matrixMaxLen(matrix) -> int:
    maxWidth = 0
    for row in matrix:
        maxLen = len(str(max(row, key=lambda x: len(str(x)))))
        if maxLen > maxWidth:
            maxWidth = maxLen
    return maxWidth + 1

def printMatrix(matrix):
    outFormat = ("{:" + str(matrixMaxLen(matrix)) + "}") * len(M[0])
    for row in matrix:
        print(outFormat.format(*row))

printMatrix(M)
