# define: just like set, but with customly defined keys
# These are unordered, and mutable datatype.

# syntax: my_dict = {key: value, key2: value2}
# or using dict() function: 
# 

my_dict2 = dict(name= "Hamza", age= 18, gender= "Male")
print(my_dict2) # {'name': 'Hamza', 'age': 18, 'gender': 'Male'}

# important notes about keys in python dictionaries
# note: value can be of any datatype, but key is preffered to be either number or string or tuple which are immutable objects. 

# note: a key is always unique, on the other hand, there can be same value assigned to multiple keys.

# syntax: accessing a dictionary value-> using the key name inside square bracket or using .get() method by passing it the key name as argument

print(my_dict2["name"]) # Hamza

print(my_dict2.get("age")) # 18

# syntax: since dictionaries are mutable we can directly update the values using their access

# modifying multiple values in a dictionary at once:
# syntax: dict.update(anotherDict) allows us to modify multiople values in a dictionary. if the key is already present in orginal dict the value is updated to the anotherDict's value and if the key is not present in dict it will be added as a new key-value pair in dict

newDict = {"gender": "male", "age": 25, "address": "Saidpur, Islamabad"}

my_dict2.update(newDict)
print(my_dict2) # {'name': 'Hamza', 'age': 25, 'gender': 'male', 'address': 'Saidpur, Islamabad'}

my_dict2["name"] = "Hamza Raheem"

print(my_dict2["name"]) # Hamza Raheem

# syntax: to delete a key-value pair in a dictionary use the .pop(key) method

my_dict2.pop("gender") # it also returns the value stored corresponding to the key
print(my_dict2) # {'name': 'Hamza Raheem', 'age': 25, 'address': 'Saidpur, Islamabad'}

# another method to delete a key-value pair is to use .popitem() method which removes the last added key-value pair from the dictionary.

# syntax: to add a new key-value pair, you can either

# i) use direct assignment operator to achive this

my_dict2["University"] = "NUST"
print(my_dict2) # {'name': 'Hamza Raheem', 'age': 25, 'address': 'Saidpur, Islamabad', 'University': 'NUST'}

# ii) use .setDefault(key, value) method

my_dict2.setdefault("isFeminist", True)

print(my_dict2) # {'name': 'Hamza Raheem', 'age': 25, 'address': 'Saidpur, Islamabad', 'University': 'NUST', 'isFeminist': True} 

# to enumerate a dictionary, we cannot directly use the enumerate function because it will give us a tuple that will contain computer generated indexing from 0 -> n with key

# we have to use .items() method to enumerate a dictionary like we enumerate other collections

my_dict = {"one": 1, "two": 2, "three": 3}

# for key, item in my_dict.items():
#     print(key, item)

# one 1
# two 2
# three 3

# note: .values() method to get a list of all the values and .keys() to return a set-like structure of keys in a dictionary.

# nested dictionaries are also allowed

nested_dict = {
    "one": {'01': 1, '1': True}
    , "two": {'10': 2, "2": 'bisexual'}
    , "three": {'11': 3, '3': 'cheating'}
    }

# print(nested_dict) # {'one': {'01': 1, '1': True}, 'two': {'10': 2, '2': 'bisexual'}, 'three': {'11': 3, '3': 'cheating'}}

