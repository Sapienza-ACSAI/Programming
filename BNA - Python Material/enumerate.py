# enumeration

def grocerylist():
    grocery = ['bread', 'milk', 'butter']
    total = 0
    for count, item in enumerate(grocery): # this assings numbers to count and items to item by default
      # this is enumaration in python
      total += count
    return total

print(grocerylist())