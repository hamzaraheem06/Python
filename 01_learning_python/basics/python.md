# Python: A Cool Programming Language

"Python is a cool language, and JavaScript is a vibe-based language. C++ is for nerds and Java is for braindead." ~ Hamza, 2025

## Internal working of Python:

In other fundamental programming languages like C/C++, Java, etc., the source code is converted to machine code, machine code gives direct instructions to the computer hardware.

However, Python code is firstly compiled to something called as Byte Code (.pyc).

_Byte Code is not a machine code. It cannot give direct instructions to CPU. This is done for the sake of optimization when we import multiple modules in a file. It doesn't happen when we work on a single or a top level file because there is no need of further optimization as there is one long single code that can be interpreted directly._

To execute/interprete this Byte Code, Python has a Python Virtual Machine (PVM) which interpretes this code and we get the output.

### **A simple flow chart of this would be:**

_Python Code (.py) ---(compiling)---> Byte Code (.pyc) ---(PVM)---> Output_

## Immutability and Mutability in Python:

Immutability refers to that any reference to value in memory is unchangable. It doesn't mean that the variable's value can't change.

_When you modify an immutable object, a new object is created, and the variable is updated to reference the new object._

Lets understand this with a code:

```python
username = "Hamza"

print(id(username)) # 1746254057360

username = "Ayesha"

print(id(username)) # 1746254057408
```

username = 'Hamza' will create an object in memory which will contain 'Hamza', and then username will point to it.

If we change the username's value to 'Ayesha', an another object containing 'Ayesha' will be created and then the username will point to it.

_Notice how there has been no change in original 'Hamza' object, this is what Immutability means in Python_ and since there is a garbage collector provided in Python, the 'Hamza' object is automatically deleted by the garbage collector.

**NOTE: The variable itself doesnot contain information about the datatype of the value it is pointing to. The datatype is stored in the memory.**

Now lets start with Mutability.

_Any changes in mutable object , affect all references to the object._

Lets understand it with a code:

```python
a = [1, 2, 3]
b = a

a is b # True

a[0] = 44

print(a) # [44, 2, 3]
print(b) # [44, 2, 3]
```

**What happened here?**

You might get surprised how a and b have same value when we clearly watched how in above example the reference changed after we changed the values?

Here is where the concept of Mutability comes in. Since a list is mutable, the reference doesn't get change after modification in either of the memory reference.

However, if we explicity change the value of either of the variables i.e. we assign it a new object, as in the following code, then the a new reference will be created and that varialbe will point to the new reference.

```python
a = [1, 2, 3]
b = a

a == b # True
a is b # True

a = [1, 2, 3]

a == b # True
a is b # False
```

Let's understand it:

When the line 1 will get executed a memory reference containing a list [1,2,3] will be created and then a will point to it, simple right?

Then in line 2, b = a means b should point to a reference that a is pointing.

Therefore, when we used is operator in line 4 we get True.

Then in line 5 we explicity assign the same value to a again. Then a new reference is created and a then points to new reference.

That's why, altough they have same value but a different memory address.
