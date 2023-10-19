# Programming Unit 1

# --------------------- Lesson 5 ---------------------

"""
About OBJECTS:
A program is made up of many cooperating objects, so that it's simpler to divide the problem and solve it. Objects
make use of each other's capabilities.

Technically an object is a bit of self-contained Code and Data. Objects have boundaries, that allow us to ignore those
un-needed data: this means that an object doesn't know the details of other objects, and gives us the capability of
not consider the details of the rest of the code. Objects are stand-alone, an object can't access the data inside
another object.

A program receives an input, which passes from object to object and, after passing through all the required objects
determined by the algorithm, it becomes our output.

Here are some definitions:
- CLASS:
         A CLASS is a template: all the items inside this class have the same properties (for example all the STRINGS
         have the same properties).

  --> D: More properly, a class defines the abstract characteristics of a thing (object), including its characteristics
         (so its ATTRIBUTES, FIELDS or PROPERTIES) and its behaviours (so its capabilities, its METHODS, features or
         operations).

         We may say that a class is a sort of blueprint of the objects that come from such blueprint;

- METHOD or MESSAGE:
         A METHOD is a defined capability of a certain class (for instance, a list has the .sort() method,
         or for example a string has the .split() method; each class has its own methods);

  --> D: METHODS are the objects' abilities. They may be considered as the verbs in programming. Within the
         program, using a method usually affects only one particular object (for example all Dogs can bark,
         but you need only one particular dog to do the barking).

- FIELD or ATTRIBUTE:
  --> D: An ATTRIBUTE is a bit of data in the class, which defines some characteristics of the objects within that same
         class.

- INSTANCE:
  --> D: One can have an instance of a class or a particular object. The instance is the actual object created
         at runtime. In programmer jargon, the "Lassie" object is an instance of the Dog class. The set of values of
         the attributes of a particular object is called its state. The object consists of state and the behavior
         that's defined in the object's class.
"""


# For example, this is a class:

class MyFirstClass:  # This is the template for making the objects related to the class MyFirstClass
    x = 0  # Each MyFirstClass object has a bit of data

    def myTest(self):  # SELF is needed to tell Python that it has to edit the data inside the class
        self.x += 1
        print(f"We got {self.x}")  # Each MyFirstClass object has a bit of code

    #                                 We remember that each object is made of bits of both CODE and DATA


container = MyFirstClass()  # We construct a MyFirstClass object, and we store it in a variable
#                                     called "container"

container.myTest()  # Doing so allows us to tell the "container" object to run its code, so the function
#                                     myTest(). In other words, we are executing the myTest() function.

# We can use the dir() function to find the capabilities of our Class

print(dir(MyFirstClass()))

print("\n")  # Separator
'''
Objects are created, used and discarded. There are some parts of code that get called when:
    - an object is created (CONSTRUCTOR);
    - an object is destroyed (DESTRUCTOR).

While constructors are used more frequently in Python, Destructors are seldom used. The primary purpose of the
constructor is to set up some instance variables to have the proper initial values when the object is created

 --> D: In object oriented programming, a constructor in a class is a special block of statements called when an
        object is created.
'''


# This is an example of a class having a constructor:

class SecondClass:
    x = 0
    name = ""  # We leave "name" blank, since it will be filled everytime we call the class

    def __init__(self, z):
        self.name = z
        print(f"You inserted the name {z}")

    def secondTest(self):
        self.x += 1
        print(f"{self.name} is the name number {self.x}")

nadia = SecondClass("Nadia")
mauman = SecondClass("Mauman")
spognardi = SecondClass("Spognardi")

nadia.secondTest()
mauman.secondTest()
nadia.secondTest()
spognardi.secondTest()

"""
Each object (nadia, mauman and spognardi) has its own values that are stored inside the class. It's useful to make a
class when there are a LOT of items with the same common properties
"""

print("\n")  # Separator

#---------------------------------------------------- Example #1 ----------------------------------------------------

class SapienzaProfessors:
    name, surname, age, subject, department = "", "", 0, "", ""

    def __init__(self, i_name, i_surname, i_age, i_subject, i_department):
        print(f"---You inserted---\n{i_name} {i_surname}, {i_age}\nTeaching {i_subject} at {i_department}\n---Are those data correct?---")
        checkInput = input("Y/N: ")
        if checkInput.lower() == "y":
            self.name, self.surname, self.age, self.subject, self.department = \
                i_name, i_surname, i_age, i_subject, i_department
            print("The data were inserted in the database")
        elif checkInput.lower() not in ["y", "n", "Y", "N"]:
            raise ValueError("Please insert a valid input. Accepted inputs are Y and N")
        else:
            print("The data were not inserted in the database")

    def changeDepartment(self, newDepartment):
        self.department = newDepartment

    def printAllInfo(self):
        print(f"---Professor Info---\n{self.name} {self.surname}, {self.age}\nTeaching {self.subject} in {self.department}")


prof0 = SapienzaProfessors("Maurizio MauMan", "Brumotti", 28, "Nothing", "ICT Engineering")
prof0.printAllInfo()
