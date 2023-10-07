                                                                                                                                                
"""CLASSES"""

class Employee:
    name = ""
    age = 0
    cv = ""
    address = ""
    
    def __init__(self, i_name, i_age, i_cv, i_address): # a constructor
        self.name = i_name
        self.age = i_age
        self.cv = i_cv
        self.address = i_address

    def ChangeAddress(self, newAddress : str):
        self.address = newAddress
        
    def Print(self):
        print(self.name, self.age, self.cv, self.address)


# E0 = Employee()
# print(type(E0)) # <class '__main__.Employee'>

# E0.age = 48
# E0.cv = "folder/E0_cv.pdf"
# E0.address = "Via Palestro, 7"
# E0.name = "Maurizio Mancini"

# E0.Print() # Maurizio Mancini 48 folder/AS_cv.pdf Via Palestro, 7


# after the initialization you can just do:
    
E1 = Employee("Nadia Ansini", 69, "folder/E1_cv.pdf", "Poop Street")

E1.Print()