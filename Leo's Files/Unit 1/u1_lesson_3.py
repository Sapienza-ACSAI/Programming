# Programming Unit 1

# --------------------- Lesson 3 ---------------------

# When we talk about recurrence, we mean a function that calls itself.

def benches(row):
    counter = 1
    if row != 0:
        counter += benches(row - 1)
    else:
        pass
    return counter

print(benches(10))

def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n-1)


print(recursive(5))

def recursiveACounts(stri):
    if len(stri) != 0:
        if stri[0] == "a":
            return 1 + recursiveACounts(stri[1:])
        else:
            return recursiveACounts(stri[1:])
    else:
        return 0

print(recursiveACounts("Today it will rain, but we won't catch it since we are good at dodging rain droplets"))