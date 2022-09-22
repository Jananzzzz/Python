






'''
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
else: print("the file to be removed not exists.")
# remove a folder:
os.rmdir("myfolder")
'''

'''
f = open("test.txt", "w")
f.write("Janan wrote this file.")
f = open("test.txt", "r")
print(f.read())
f = open("newfile.txt", "x")
f.close()
'''

'''
f = open("text.txt", "a")
f.write("now the file has been compiled by Janan Zyu")
f = open("text.txt")
print(f.read())
'''

# a will append at the end of the file 
# w will overwrite all the things in the file

'''
f = open("text.txt")
#print(f.read())             # it will also read the space line at the end of the file.
#print(f.read(1))             # while opening a file, all the read function below start reading where the last reading function ends
#print(f.readline())
#print(f.readline())              # there will generate a new space line between two readline function
for x in f:
    print(x)               # read line by line  , also generate a new space line
# it is a good practice when you read a file and close it after you have done with it.
f.close()

'''

# f = open("text.txt")
# there are 4 mode when opening a file
# r: open for read, error is not exist
# a: open for append, create the file if not exist
# w: open for writing, create the file if not exist
# x: create the specified file, error if the file already exist


'''
name = "janan"
age = 20
txt = "her name is {1}, {1} is {0} years old."
print(txt.format(age, name))
'''


'''
try:
    f = open("text.txt")
    try:
        f.write("test write function")
    except:
        print("there exists some problem while writing to the file")
    finally:
        f.close()
except:
    print("something went wrong while open the file")
'''
'''
try:
    print(2)
except:
    print("an exception occurred")
'''

'''
print(max(1, 3, 2), abs(-7), pow(3, 2))
import math
print(math.sqrt(64))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)
'''

'''
import mymodule
mymodule.greeting("Janan")
print(mymodule.person["name"])
print(mymodule.person["vocation"])
# you can use dir to list all the functions and properties in a module
x = dir(mymodule)
print(x)
'''


"""
# use loop to iterate a tuple:
tuple = ("apple", "huawei", "samsung")
for x in tuple:
    print(x)
string = "iphone"
for x in string:
    print(x)
"""

'''
mytuple = ("apple", "banana", "cherry")
iterator = iter(mytuple)
print(type(iterator))        # every elements has a type
print(next(iterator))
print(next(iterator))
print(next(iterator))

# strings are also iteratable:

mystring = "apple"
iterator1 = iter(mystring)
print(next(iterator1))
'''


'''
class Person():
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname  = lname 
    
    def printname(self):
        print(self.firstname, self.lastname)                # the output of printing print() is none

me = Person("Janan", "Zyu")
me.printname()

class Student(Person):   # student will inherit the properties and methods in person, not the value
    pass

you = Student("Mike", "Jackson")
you.printname()

# if add a __init__ function in Student, then it won't inherit the Person's init function

'''



'''
class person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def returnage():
        return 20
    
    def myfunc(self):
        return("hello my name is: " + self.name)       # if use print instead of return, then the output will have a None behind it
                                                    # which reflects the function has a print operation instead of return.

p = person("Janan Zyu", 20)
p1 = person("janan", 31)
# print(p.name)
# print(person.returnage())
# print(p.myfunc())

# infact, you can delete a property or delete a object:
del p.age

print(p.name)
print(p1.age)
'''



