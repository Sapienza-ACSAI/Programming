'''learned about the easy approach'''

# Write a function that takes a string containing a series of words separated by spaces and constructs an array in which the keys are the first letters of the words in the string and the values associated with them are the lists with the words starting with that letter. The lists must have a lexicographical order.

def remove_nonalpha(word):
    newword = ''
    for char in word:
        if char.isalpha():
            newword += char
    return newword

def starting_letter_words(a_string: str):
    wlist = a_string.lower().split()
    wlist = map(remove_nonalpha, wlist) 
    d = {chr(c):[] for c in range(ord('a'), ord('z')+1)}
    
    for word in wlist:
        if word not in d[word[0]]:
            d[word[0]].append(word)
    
    d = {k:v for k,v in d.items() if v}
    
    for l in d.values():
        l.sort()
        
    return d

# print(starting_letter_words("It is better to be the hammer than the nail."))
# print(starting_letter_words("If I had your marks, I would never do your missing marks!"))

# ------------------- Exercises for Wednesday 16/11 on Q2A

# Write a function that takes a dictionary in which each key is a string, its value is an integer, and returns the ordered list of all keys matched by an even value. 
# For example, for the dictionary { 'mikey mouse':12, 'pluto':3, 'minnie':7, 'foo':4, 'here':3 } the function must return the list ['foo','mikey mouse'].

def dictionary_evens(d):
    return sorted([key for key in d if d[key] % 2 == 0])        

# Write a function that takes a dictionary of the type {key:integer list} and returns a new dictionary with the same keys but as the value the average of the integers in the original dictionary list.

def dict_average(d):
    return {key: int(sum(d[key]) / len(d[key])) for key, value in d.items()}
        
# Write a function that takes two {key:set} dictionaries and returns a new dictionary in which only the keys in both input dictionaries are present, and the values are the union of the two input sets associated with the same key

def double_dictionary(d1, d2):
    newd = {}
    for key in d1:
        if key in d2:
            newd[key] = d1[key].union(d2[key])
    return newd

def double_dictionary(d1,d2):
  return {k: d1[k]|d2[k] for k in d1 if k in d2}

# Write a function that takes a string of words separated by spaces and constructs a dictionary in which the keys are the lengths of the words, and the values are sets with the words that have exactly that length in numbers of characters.

def dict_of_word_len(word_str):
    
    # return {len(word): [w for w in word_str.split() if len(w) == len(word)] for word in word_str.split()}
    d = {}
    for word in word_str.split():
        d.setdefault(len(word), []).append(word) # set default sets the value if it doesnt exist, if it does, continues on
        # in this case, if it doesnt exist [] if it exists, appends
    return d

print(dictionary_evens({ 'mikey mouse':12, 'pluto':3, 'minnie':7, 'foo':4, 'here':3 }))
print(dict_average({'gas':[100, 200, 150], 'electricity':[382, 120, 100]}))
print(double_dictionary({'A': {1, 2, 3, 4}, 'B': {3, 4, 5, 6}, 'C':{7, 8}}, {'A': {2, 3, 4, 5}, 'B':{3, 4, 5, 6, 7}, 'D':{10, 11, 12, 13}}))
print(dict_of_word_len('hello        my   name is leon smith          '))