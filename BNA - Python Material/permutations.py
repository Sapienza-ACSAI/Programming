
# - - - - - - - Exercises for 9th of December, Friday (Online Lecture)
# Write a function that evaluates all the permutations of a string in input
# 'abc' -> 'abc,acb,bca,bac,cab,cba'

def permutations(string):
    if len(string) == 1:
        return [string]

    ret = []
    for i, char in enumerate(string):
        smaller_permutations = permutations(string[:i]+string[i+1:])
        for s in smaller_permutations:
            ret.append(char+s)
    return set(ret)

print(permutations('abc'))