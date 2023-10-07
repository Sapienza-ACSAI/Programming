
# give 20% discount if there are more than 20 students
students = int(input("Number of students in group: "))
fullPrice = 5

def museum_cost(people, ticket):
    if people >= 20:
        singlePrice = (ticket / 100) * 80 #calculate discount
        priceInt = singlePrice * people
        price = "The price with the discount of 20% is " + str(priceInt) + "€ because there are " + str(people) + " students"
        return price
    else:
        priceInt = ticket * people
        price = "The price without the students discount is " + str(priceInt) + "€ since there are " + str(people) + " students and you need at least 20"
        return price

print(museum_cost(students, fullPrice))


# a function that asks the user for integers until the user inserts 0.
# It returns the NUMBER OF negative values insterted.

def negative_numbers():
    count = 0
    while True:
        c = int(input("yo gimme an integer: "))
        if c < 0:
            count += 1
        if c == 0:
            break # the break only breaks ONE while statement
    print ("you inserted",count, "negative numbers")


def average_from_input():
    count = 0
    total = 0
    x = int(input("insert a number:"))
    while x != 0: # if x is different than 1
        total = total + x
        count += 1 # add 1 to the existing number of numbers
        x = int(input("insert a number:"))
    print ("The average is", total / count)
    


# WITH THE BREAK STATEMENT - break takes you out of the loop

# def average_from_input():
#    count = 0
#    total = 0
#    x = int(input("insert a number:"))
#    while x != 0: # if x is different than 1
#        total = total + x
#        count += 1 # add 1 to the existing number of numbers
#        x = int(input("insert a number:"))
#        if x == 0:
#            break
#    print ("The average is", total / count)



