class Car:
    count = 0 # class variable or static variable you know what it means hamza, static variables are declared and initialized outside any method i.e. in the class scope. they are same for each instance of the class and can be accessed using the class name as well as instance name
    def __init__(self, model, year):
        self.model = model # instance variables defined inside the constructor. can also be added or deleted or modified on the way using the methods appended below. These are unique to each instance of the class.
        self.year = year
        Car.count += 1

    def display(self):
        print(f"Model: {self.model} \nManufacture year: {self.year}")

car1 = Car("Mercedes", 1999)

# car1.__init__("Mercedes", 1998)

car1.display()

setattr(car1, "year", 2003)

setattr(car1, "Owner", "ABC")

delattr(car1, "Owner")

car1.display()

# print(getattr(car1, "MODEL")) # AttributeError: 'Car' object has no attribute 'MODEL'

print(Car.__dict__)




    # getattr(obj, name[, default]) − to access the attribute of object.
    #
    # hasattr(obj,name) − to check if an attribute exists or not.
    #
    # setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
    #
    # delattr(obj, name) − to delete an attribute.

# to hide data from outside classes use __attrName to declare the attribute which will not be directly accessible to the classes outside

class DizNuts:
        def __init__(self, name, age):
            self.__age = age
            self.__name = name

        def display(self):
            print(f"Name: {self.__name}")
            print(f"Age: {self.__age}")


nut1 = DizNuts("Hamza", 18)
nut1.display()

# print(nut1.name) # AttributeError: 'DizNuts' object has no attribute 'name'

# Python protects those members by internally changing the name to include the class name.
# You can access such attributes as   object._className__attrName.

# print(nut1._DizNuts__name) # Hamza

# Python doesnt have the public, protected or private keyword for data encapsulation. by default all the members are pulbic and to achieve the functionality of private use __ before variable name, and _ for protected. these are accessed in the same manner by underscores.