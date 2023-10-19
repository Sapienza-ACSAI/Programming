# Programming Unit 2

# --------------------- Lesson 14 ---------------------

def palindrome(word):
    word = word.replace(" ", "")
    if len(word) < 2:
        return True
    if word[0] == word[-1] and palindrome(word[1:-1]):
        return True
    else: return False

'''def palindromePrevious(word):
    word = word.replace(" ", "")
    cLeft, cRight = 0, -1
    if (word[cLeft] == word[cRight]) and (0 <= cLeft <= len(word)):
        cLeft += 1
        cRight -= 1
        palindrome(word)'''

print(palindrome("i topi non avevano nipoti"))