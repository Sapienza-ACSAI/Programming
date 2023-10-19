# Programming Unit 2

# --------------------- Lesson 9 ---------------------

# A dictionary holds various keys and for each key there is a corresponding
# value. A dictionary has the following structure:

myDict = {
    "value_1": 13543,
    "value_2": 76568,
    "value_3": "A Value",
    "value_4": ["A",
                "Value",
                "Could",
                "Be",
                "A",
                "List",
                "Like",
                [
                    234,
                    645,
                    867
                ]],
    "value_5": True
}

# We can recall values via the "index" way

print(myDict["value_3"])

# Items in a dictionary can be also edited like this:

myDict["value_3"] = "A New Value"

print(myDict["value_3"])

# We can even convert tuples into dictionaries using the dict() function

toConvert = [("hello", 543), ("world", 645), ("hey", 697)]

newDict = dict(toConvert)

print(newDict)

# Quick overview about formatted strings:

formDict = {
    "one": "test",
    "two": 6435,
    "three": 695
}

for key, value in myDict.items():
    print(f"Example 1 - The key {key} holds the value {value}")
    print("Example 2 - The key {} holds the value {}".format(key, value))

# We can even delete keys and values, using multiple methods:
# - the del() function;
# - the pop() method;

del formDict["two"]

print(formDict)

formDict.pop("three")

print(formDict)


# Write a function that takes as input a list of elements and builds and returns
# a dictionary where the keys are the elements of the list and the values are the
# number of repetitions of that element in the list

def dicOfReps(array):
    solDict = {}
    while len(array) != 0:
        howMany = array.count(array[0])
        solDict[array[0]] = howMany
        for i in range(howMany):
            array.remove(array[0])
    return solDict


print(dicOfReps([1, 1, 1, 2, 2, 4, 5, 7, 7, 7, 7, 7, 8, "a", "a", "a", "b", "b", "c", "aaa", "bruh"]))
