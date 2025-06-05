class Car:
    count = 0
    def __init__(self, model, year):
        self.model = model
        self.year = year
        Car.counter()

    def drive(self):
        print("Driving")

    # class methods are the methods that are called on a class reference. these are defined using the @classmethod decorator and have access to cls parameter which i am assuming is the python equivalent of this as in java. NOPE. cls is a convention used in class methods to refer to the class itself, typically in the context of a @classmethod.
    # cls is used to access or modify class-level data (e.g., static attributes) or to create alternative constructors

    @classmethod
    def counter(cls):
        cls.count += 1 # modify

    @classmethod
    def display_count(cls):
        print(cls.count) # access

    @classmethod
    def add_car(cls, model, year):
        return cls(model, year) # alternative constructor

car1 = Car("Mercedes", 1999)

car2 = Car.add_car("Porsche", 1999) # using the alternative constructor

Car.display_count() # 2

# unlike other programming languages, we can add class methods on the go in python. define a method with @classmethod and use setattr method to add the reference to the class

@classmethod
def dummy_method(cls):
    print("This is a test method")

setattr(Car, "test", dummy_method)

Car.test() # This is a test method

# delete a class method

del Car.test

# calling after deleting the method
# Car.test() # AttributeError: type object 'Car' has no attribute 'test'

# another type is static methods which are just as same as static methods in java. They are defined with the @staticmethod decorator and can only access static fields.

class DizNuts2:
    username = "Nutty Nathan"

    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    @staticmethod
    def give_backshot():
        print(f"Backshot for {DizNuts2.username}!") # Backshot for Nutty Nathan!

my_obj = DizNuts2(19, "dragon")
DizNuts2.give_backshot() # accessing using class reference

# PYTHON DOES NOT ALLOW MULTIPLE CONSTRUCTORS BUT YOU CAN USE *args TO DO CONDITIONAL INITAILZATION BASED ON THE NUMBER OF ARGUMENTS PASSED. 