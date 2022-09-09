complex_number = complex(2,3)
print(complex_number)
x1 = 3
print(float(x1))
# float() can convert integer numbers to floating-point numbers
# note that it doesn't work on complex numbers 
print(int(2.3))
print(int(10.7))
# int() can convert float numbers to integer(cutting the numbers behind the decimal) 
# also can't be used on complex numbers and string representing numbers
10.0.is_integer()
10.2.is_integer()
(10).bit_length()

print(10.0.is_integer())
print(10.2.is_integer())
print((10).bit_length())     # 10 is 1010

print((16).bit_length())     # 16 is 10000 
# that is, length is the binary length of a number.
print((16).bit_count())
print((10).bit_count())
print((10).bit_count())
# bit_count is the length of the number of "1" appeared in the binary number.

greetings0 = 'hello, python'
greetings1 = "hello, python"
greetings2 = "'hello,python'"
greetings3 = """hello, python"""

print(greetings0)

print(greetings1)
print(greetings2)
print(greetings3)
print("hello," + " " + "python")
print(len("hello, python"))
print("hello, python".upper()) # so is .lower()


name = "Janan Zhu"
age = 19
print("My name is {0}, and my age is {1}".format(name, age))
print(f"My name is {name}, and my age is {age}")
print("My name is {0}, and my age is {1}".format(age, name))
print("My name is {0}, and my age is {1}".format(name, age))

welcome = "hello, python"
print(welcome[0])
print(welcome[0:7])

# lists are usually called arrays in nearly every other programming language.
empty = []
print(empty)
numberlist = [1, 2, 3, 4]
print(numberlist)
numberlist[3] = 200
print(numberlist)
# list of strings
ListOfStrings = ["hello", "python"]
print(ListOfStrings)
ListOfDifferentTypes = ["Hellopython", [1, 3, 5], False]
print(ListOfDifferentTypes)
print(ListOfDifferentTypes[-1])
# negative indices retrieve items in reverse order

numbers = [1, 2, 3, 4]
newnumbers = numbers[0:2]
print(newnumbers)
print(ListOfDifferentTypes[1][2],ListOfDifferentTypes[0][2])


# concatenate strings
fruit0 = ["apple"]
fruit1 = ["grape"]
fruit2 = fruit0 + fruit1

print(ListOfDifferentTypes[1][2],ListOfDifferentTypes[0][2])
print(fruit2)
fruit0.append("tree")
print(fruit0)
fruit2.sort()
print(fruit2)
# above the .sort() function and .append() function is most useful
# the next i will write a .pop() function, which is to remove an item from the list
fruit2.pop(1)
print(fruit2)

# the next part is tuple.
# the differences between tuple and list is that tuple is immutable sequences. 
# in this case, a list is more like an address, on which you can put anything you want to put.
employee = ("Janan", "Zhu", 19, "Data Scientist")
print(f"Hello, my name is {employee[0]}.\nI am {employee[2]} year old.")
# above shows that indexing and slicing tuples are allowed
# concatenation operation is okay, too
# len() returns the number of items in tuple
print(len(employee))

# list can turn a tuple into a list
list(employee)
print(list(employee))

# tuple has two built-in function: count and index
# count is to count the number of times of a specific item appears in the underlying tuple
letters = ("1", "1", "2", "3")
print(letters.count("a"))
print(letters.count(1))
# if the specific item is not in the underlying tuple, it returns 0

# .index() returns the index of the first istance of that object in the underlying tuple
# if not in the tuple, it raise a valueerror
print(letters.index("2"))

# now here comes the very important part of python: dictionary.
# which in my tuition is sort of a database
# below are two ways of representing a dictionary:
person0 = {"name": "Janan Zhu", "age": 19, "title": "advanced data scientist"}
# using curly bracket and colon to divide
person1 = dict(name = "Janan Zhu", age = 19, title = "advanced data scientist")
print(person0)
print(person1)







