# Programming Unit 2

# --------------------- Lesson 10 ---------------------

# Write a function that takes as input a list of elements and a filename.
# It saves in the file with input name each element in the list and the
# number of times it is repeated in the list. Each element is saved only
# once and the number of repetitions is saved separated by a tab character.
# The order in which each element appears in the file is the same of the
# input list

myList = [1, 1, 1, 7, 7, 3, 3, 3.4, 3.4, 3.5, "house", "a", "a", 1]

def printElems(array, filename):
    with open(filename, "w", encoding="UTF-8") as exFile:
        while len(array) != 0:
            howMany = array.count(array[0])
            whatToWrite = str(array[0]) + "    " + str(howMany)
            print(whatToWrite, file=exFile, end="\n")
            for i in range(howMany):
                array.remove(array[0])

if __name__ == "__main__":
    printElems(myList, "u2_lesson_10_solution.txt")