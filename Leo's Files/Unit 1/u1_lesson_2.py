# Programming Unit 1

# --------------------- Lesson 2 ---------------------

# Computers use files to store any data, since a file is persistent, while
# for example program runtime data are temporary, ephemeral.
# There are two types of files that interest us:
#  - Text files:
#     - they contain printable text characters only, and they are convenient
#       for any program;
#     - they can be read/modified with simple text editor tools;
#     - they are not system/program dependant;
#  - Binary files:
#     - for example .jpg files, .docx files, etc...;
#     - without a certain program, they are not humanly readable;
#     - they are system/program dependant.

# A Python text file contains a linear sequence of characters, they are
# encoded in ASCII or Unicode, and are separated into lines. Files are
# processed either in "read only" or "write only" mode.

# To open a file with Python (which is considered as an iterable object) we
# write like this:

fileRef = open("Assets/u1_lesson_2_asset_1.txt", "r", encoding="utf8")


# The open() function asks for 3 inputs:
#  - a path for the file, starting from the folder where the Python file is;
#  - if the file is in:
#     - read-mode we write "r";
#     - write-mode we write "w";
#  - the encoding format. <------ IT'S IMPORTANT IN ALL THE HOMEWORKS TO SPECIFY IT
#
# Syntax: open("path/to/file.txt", "r/w", encoding="utf8")

# We can use the for loop to iterate through the file:

def firstFile():
    for l in fileRef:
        print("Line: ", l)

fileRef.close()


# It's important to close the file when we don't need it anymore. We can reopen it
# anytime we want. The file can be opened only once at a time, so it's important to
# close it when not necessary anymore

def secondFileFunc():
    secondFile = open("Assets/u1_lesson_2_asset_2.txt")

    for line in secondFile:
        if int(line) % 2 == 0:
            print(line, "is an even number")
        else:
            print(line, "is an odd number")

    secondFile.close()

# secondFileFunc()

#--------------------- Exercise 1 ---------------------

# Write a function that, given a text file name as parameter,
# counts and returns the number of characters and lines
# in the file

# Newline characters should not be counted

def NumCharsAndLinesInFile(textFile: str) -> (int, int):
    myFile = open(textFile, "r", encoding="utf8")
    nL = 0
    nC = 0
    for fLine in myFile:
        char = len(fLine)
        nC += char
        nL += 1

    print("The file contains %i characters and %i lines" % (nC, nL))

# NumCharsAndLinesInFile("Assets/u1_lesson_2_asset_3.txt")

#--------------------- Exercise 2 ---------------------

# Write a function that counts and returns the number of
# odd and even numbers in a given text file

# The text file name is provided as a parameter to the function

# The file contains some integer numbers separated by
# any number of spaces and on different lines
# (lines can also be empty, or contain spaces only)

# For example, CountOddEvenInFile("u1_lesson_2_asset_4.txt") has to
# return (5, 7)

def CountOddEvenInFile(fileName: str) -> (int, int):
    myFile = open(fileName, "r", encoding="utf8")
    odd = 0
    even = 0
    for fileLine in myFile:
        sepLine = fileLine.split()
        for char in sepLine:
            if char != "":
                char = int(char)
                if char % 2 != 0:
                    odd += 1
                else:
                    even += 1
    print(odd, even)
    myFile.close()

CountOddEvenInFile("Assets/u1_lesson_2_asset_4.txt")

# Python gives the possibility to store exceptions in the code:
# with the try-except block we can give instructions that must
# be followed until we reach a certain exception. The block
# works as the following:

'''
try:
    <Code to be executed>
except <exception>:
    <Code to execute when the exception happens / is met>
    '''
