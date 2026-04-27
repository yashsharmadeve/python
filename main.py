# 1. Data Types 

# String
name = "John Doe"
print(name)
print(type(name))

# Integer
age = 30
print(age)
print(type(age))

# Floatheight = 5.9
height = 5.9
print(height)
print(type(height))

# Booleanis_student = True
is_student = True
print(is_student)
print(type(is_student)) 

# 2. print and output - in console
print("Hello, World!")
print("My name is", name, "and \n I am", age, "years old.") # \n for next line

# 3. Variables and Constants
# Variables can change their value
x = 10
print(x)
x = 20
print(x)

# Constants are usually defined in uppercase and should not change
PI = 3.14159
print(PI)

# 4. Input and User Interaction
user_name = input("Enter your name: ") # gives string input from user
print("Hello, " + user_name + "! Welcome to Python programming.")

# 5. Arthmetic Operations
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", int(a / b)) # using int() to get integer result
print("Modulus:", a % 6) # gives remainder
print("Exponentiation:", a ** 2) # a raised to the power of 2
print("Floor Division:", a // b) # gives quotient without remainder

# 6. string methods
greeting = "Hello, World!"
print(greeting.upper()) # converts to uppercase
print(greeting.lower()) # converts to lowercase
print(greeting.capitalize()) # capitalizes the first letter of the string
print(greeting.startswith("Hello")) # checks if string starts with "Hello"
print(greeting.endswith("!")) # checks if string ends with "!"
print(greeting.find("World")) # finds the index of "World"
print(greeting.count("o")) # counts the number of occurrences of "o"
print(greeting.replace("World", "Python")) # replaces "World" with "Python"
print(greeting.split(", ")) # splits the string into a list based on the delimiter ", "
print(greeting.strip("!")) # removes "!" from the end of the string
print(greeting[0]) # prints the first character of the string
print(greeting[7:12]) # prints characters from index 7 to 11 ("World")
print(greeting[-1]) # prints the last character of the string
print(greeting[-6:-1]) # prints characters from index -6 to -2 ("World")
print(greeting[::2]) # prints every second character of the string
print(greeting[::-1]) # prints the string in reverse order
print(greeting.isalpha()) # checks if all characters in the string are alphabetic
print(greeting.isdigit()) # checks if all characters in the string are digits
print(greeting.isalnum()) # checks if all characters in the string are alphanumeric (letters and numbers)
print(greeting.isspace()) # checks if all characters in the string are whitespace
print(greeting.title()) # converts the first character of each word to uppercase
print(greeting.center(20, "*")) # centers the string within a field of width 20, using "*" as the fill character
print(greeting.ljust(20, "-")) # left-justifies the string within a field of width 20, using "-" as the fill character
print(greeting.rjust(20, ".")) # right-justifies the string within a field of width 20, using "." as the fill character

# 7. Conditional Operators
# == Equal to
# != Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
num1 = 10
num2 = 20
print(num1 == num2) # False
print(num1 != num2) # True
print(num1 > num2) # False
print(num1 < num2) # True
print(num1 >= num2) # False
print(num1 <= num2) # True
# cannot compare strings
str1 = "a"
str2 = "b"
print(str1 < str2) # True because "a" comes before "b" in the alphabet
print(ord(str1)) # gives the ASCII value of "a"
print(ord(str2)) # gives the ASCII value of "b"

# 8. Chained Conditionals
num1 or num2 > 15 # True because num2 is greater than 15
num1 and num2 > 15 # False because num1 is not greater than 15
not num1 > 15 # True because num1 is not greater than 15
if num1 > 15 and num2 > 15:
    print("Both numbers are greater than 15")
elif num1 > 15 or num2 > 15:
    print("At least one number is greater than 15")
else:
    print("Neither number is greater than 15")


# 9. if-elif-else statements
age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# 10. Lists/Tuples
x = [4,True,"Hello",3.14] # list can contain different data types
print(x)
print(type(x))
print(len(x)) # gives the length of the list
print(x.append("World")) # adds "World" to the end of the list
print(x.extend([1,2,3])) # adds multiple elements to the end of the list
print(x.insert(1, "Python")) # inserts "Python" at index 1
print(x.remove(3.14)) # removes the first occurrence of 3.14 from the list
print(x.pop()) # removes and returns the last element of the list
print(x.pop(1)) # removes and returns the element at index 1
print(x.index("Hello")) # gives the index of the first occurrence of "Hello"
print(x.count(True)) # counts the number of occurrences of True in the list
print(x.sort()) # sorts the list (only works if all elements are of the same data type)
print(x.reverse()) # reverses the order of the list
print(x[0]) # prints the first element of the list
print(x[1:4]) # prints elements from index 1 to 3
print(x[-1]) # prints the last element of the list
print(x[-4:-1]) # prints elements from index -4 to -2
print(x[::2]) # prints every second element of the list
print(x[::-1]) # prints the list in reverse order

y = (1, 2, 3) # tuple is similar to list but is immutable (cannot be changed after creation)
print(y)
print(type(y))
print(len(y)) # gives the length of the tuple
print(y[0]) # prints the first element of the tuple
print(y[1:3]) # prints elements from index 1 to 2
print(y[-1]) # prints the last element of the tuple
print(y[::-1]) # prints the tuple in reverse order

# 11. Loops
# for loop
for i in range(5): # iterates from 0 to 4
    print(i)
for i in range(1, 10, 2): # iterates from 1 to 9 with a step of 2
    print(i)
for char in "Hello": # iterates through each character in the string
    print(char)
for num in [1, 2, 3, 4, 5]: # iterates through each element in the list
    print(num)
x = [6, 7, 8, 9, 10]
for i in range(len(x)):
    print(x[i]) # prints each element of the list using its index

for i, element in enumerate(x): # iterates through the list with index and element
    print("Index:", i, "Element:", element)

# while loop
count = 0
while count < 5: # continues until condition is false
    print(count)
    count += 1 # increments count by 1 in each iteration

# 12. Slice operators - works on both lists and tuples
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4]) # prints elements from index 1 to 3
print(my_list[:3]) # prints the first three elements
print(my_list[2:]) # prints elements from index 2 to the end of the list
print(my_list[-3:-1]) # prints elements from index -3 to -2
print(my_list[::2]) # prints every second element of the list
print(my_list[::-1]) # prints the list in reverse order

# 13. Sets - unordered collection of unique elements - removes duplicates
my_set = {1, 2, 3, 4, 5}
x = set()   # creates an empty set 
print(my_set)
print(type(my_set))
print(len(my_set)) # gives the number of unique elements in the set
my_set.add(6) # adds an element to the set
print(my_set)
my_set.update([7, 8, 9]) # adds multiple elements to the set
print(my_set)
my_set.remove(3) # removes an element from the set (raises an error if the element is not found)
print(my_set)
my_set.discard(10) # removes an element from the set (does not raise an error if the element is not found)
print(my_set)
my_set.pop() # removes and returns an arbitrary element from the set
print(my_set)
my_set.clear() # removes all elements from the set
print(my_set)
print(1 in my_set) # checks if 1 is in the set
print(my_set.union({10, 11, 12}))
print(my_set.intersection({2, 4, 6, 8})) # gives the common elements between two sets
print(my_set.difference({2, 4, 6, 8})) # gives the elements that are in my_set but not in the other set
print(my_set.symmetric_difference({2, 4, 6, 8})) # gives the elements that are in either set

# 14. Dictionaries - collection of key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
print(type(my_dict))
print(len(my_dict)) # gives the number of key-value pairs in the dictionary
print(my_dict["name"]) # accesses the value associated with the key "name"
my_dict["age"] = 30 # updates the value associated with the key "age"
print(my_dict)
my_dict["country"] = "USA" # adds a new key-value pair to the dictionary
print(my_dict)
del my_dict["city"] # removes the key-value pair with the key "city"
print(my_dict)
print("name" in my_dict) # checks if the key "name" is in the dictionary
print(my_dict.keys()) # gives a view of all the keys in the dictionary
print(list(my_dict.keys())) # gives a list of all the keys in the dictionary
print(my_dict.values()) # gives a view of all the values in the dictionary
print(my_dict.items()) # gives a view of all the key-value pairs in the dictionary
my_dict.clear() # removes all key-value pairs from the dictionary
print(my_dict)

# 15. Comprehensions - concise way to create lists, sets, or dictionaries
# List comprehension
squares = [x**2 for x in range(10)] # creates a list of squares of numbers from 0 to 9
print(squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0] # creates a list of squares of even numbers from 0 to 9
print(even_squares)
# Set comprehension
unique_squares = {x**2 for x in range(10)} # creates a set of squares of numbers from 0 to 9 (duplicates will be removed)
print(unique_squares)
# Dictionary comprehension
square_dict = {x: x**2 for x in range(10)} # creates a dictionary where the keys are numbers from 0 to 9 and the values are their squares
print(square_dict)
even_square_dict = {x: x**2 for x in range(10) if x % 2 == 0} # creates a dictionary of squares of even numbers from 0 to 9
print(even_square_dict)

# 16. Functions - reusable blocks of code that perform a specific task
def greet(name): # defines a function that takes a parameter "name"
    return "Hello, " + name + "!" # returns a greeting message

print(greet("Alice")) # calls the function with the argument "Alice"

def add(a, b): # defines a function that takes two parameters "a" and "b"
    return a + b # returns the sum of a and b

print(add(5, 10)) # calls the function with the arguments 5 and 10

def factorial(n): # defines a function that calculates the factorial of a number n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # recursive call to calculate factorial
print(factorial(5)) # calls the function with the argument 5

def multiply(*args): # defines a function that takes a variable number of arguments
    result = 1
    for num in args:
        result *= num # multiplies all the arguments together
    return result
print(multiply(2, 3, 4)) # calls the function with multiple arguments

def func(x,y):
    return x * y, x/y # returns multiple values as a tuple

r1, r2 = func(10, 5) # unpacks the returned tuple into two variables
print("Product:", r1)
print("Quotient:", r2)

def func(*args,**kwargs): # defines a function that takes variable number of positional and keyword arguments
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    
func(1, 2, 3, name="Alice", age=30) # calls the function with both positional and keyword arguments

# 17. Scope and global variables
x = 10 # global variable
def func():
    global x # declares that we want to use the global variable x
    x = 20 # modifies the global variable x
    print("Inside function, x =", x)
func() # calls the function
print("Outside function, x =", x) # prints the modified global variable x

# 18. Raise and try-except blocks - used for error handling
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero") # raises an exception if b is zero
    return a / b
try:    result = divide(10, 0) # attempts to divide by zero
except ValueError as e: # catches the ValueError exception
    print("Error:", e) # prints the error message
finally:    print("This block will always execute") # this block will execute regardless of whether an exception was raised or not

# 19. Lambda functions - anonymous functions defined with the lambda keyword
square = lambda x: x**2 # defines a lambda function that takes one argument and returns its square
print(square(5)) # calls the lambda function with the argument 5

# 20. Map, filter, and reduce - higher-order functions for functional programming
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers)) # applies the lambda function to each element in the list and returns a new list of squared numbers
print(squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filters the list to include only even numbers
print(even_numbers)
product = reduce(lambda x, y: x * y, numbers) # reduces the list to a single value by applying the lambda function cumulatively to the items in the list
print(product)

# 21. F strings - formatted string literals for easier string formatting
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old." # uses f-string to format the string with variables
print(greeting)

