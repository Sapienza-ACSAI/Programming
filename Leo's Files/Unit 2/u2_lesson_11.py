# Programming Unit 2

# --------------------- Lesson 11 ---------------------

"""
Write a function that takes a string containing a series of words separated by
spaces and constructs a dictionary in which the keys are the first letters of the
words in the string, and the values associated with them are lists with the words
starting with that letter. The list must have a lexicographical order. Elements
in list should be repeated
"""

def removeAlpha(word: str):
    outStr = ""
    for c in word:
        if c.isalpha():
            outStr += c
    return outStr

def dicOfFirstLetters(phrase: str):
    array, outDic = phrase.lower().split(" "), dict()
    array = list(map(removeAlpha, array))
    for word in array:
        if word.isalpha():
            if outDic.get(word[0]) is None:
                outDic[word[0]] = []
            if outDic[word[0]].count(word) == 0:
                outDic[word[0]].append(word)
    for key, value in outDic.items():
        sorted(value, key=len)
    return outDic

print(dicOfFirstLetters("It is better to be the hammer than the nail. I would not do that if I were you"))

# If we have a list such as [1, 2, 3, 4, 5, 6, 7, 8, 9] we can store
# in some variables some values like the following:

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, *l = array

print(a)  # 1st element (array[0])
print(b)  # 2nd element (array[1])
print(l)  # from 3rd element to 9th element (array[3:9])
