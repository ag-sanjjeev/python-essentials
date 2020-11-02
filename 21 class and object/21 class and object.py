# class and object
class Computer:  # class definition starts here
    def specs(self):  # self is passing current object is invoked
        print("windows, 32bit")


c1 = Computer()  # defining the object for computer class

# accessing class property and method in two way
# one way mostly not preferred
Computer.specs(c1)

# another way
c1.specs()


# init method as constructor

class Company:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def details(self):
        print("The Employee ID :", self.id, " and Name : " + self.name)


e1 = Company(1, 'san')
e1.details()