print("Hello,Welcome to Python!")
print("Harohalli")
print("Kanakapura Road")
L1=[1,2,3,4,5]   #lists
print(type(L1))
#sets 
s1={1,2,3,4,5}
print(type(s1))
#tuple
s1=(1,2,3,4,5)
print(type(s1))
#complex
a=2+3j
print(type(a))
#getting keywords of python language
import keyword
print("keywords of python are:",keyword.kwlist)
b=56
print("type of value in b is:",type(b)) #knowing the type of value assigned to the variable 'b'
print("b:",b)  #printing the value stored inside the variable 'b'
c=2.0
print("type of value in c is:",type(c))
print("c:",c)
d=2+4j
print("type of value in d is:",type(d))
print("d:",(d))
name=input("What is your name ?:")
print("Helloo!!",name,"!")
#printing output as per age condition for below 18,18,and above 18
age=int(input("Enter you age:"))
if age<18:
    print("You are a kid")
elif age==18:
    print("You are an adult now!")
else:
    print("You are above 18.")
    print("hello lets start our assignment")
x=28
print(x)
y=22
print("y:",y)
print(x+y)
print("Rahul","emma","priti",25,35,56,23.87,98.06,98.04,sep=" , ")
print("Rahul","emma","priti",25,35,56,23.87,98.06,98.04, sep="\n")
print("Rahul",26 ,end=" ")
print("emma", 27, sep="\n")
# expression-> x+y where x and y are operands and + is operator or arithmetic
a=5
b=7
print(a,b)
print(a//b)
print(-3//2)
#in floor division it is floored to nearest integer 
print(a,b)
print(a*b)
print(a**b)
print(a%b)
''' comparision operators are as == checks equality,<= checks smaller and  equal,>= checks greater and equal,!= checks wwhether not equal to'''
a=6
b=3
print(a==b)
print(3==3)
print (a!=b)
print(3!=3)
print(a>b)
print(b>a)
print(6>=3)
print(3<=6)
print(3>=3)
print(2>=3)
# Demonstrating Different Operators

# Arithmetic operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print(f"a // b = {a // b}")  # Floor division

# Comparison operators
print("\nComparison Operators:")
print(f"a == b: {a == b}")  # Equal
print(f"a != b: {a != b}")  # Not equal
print(f"a > b: {a > b}")  # Greater than
print(f"a < b: {a < b}")  # Less than
print(f"a >= b: {a >= b}")  # Greater than or equal to
print(f"a <= b: {a <= b}")  # Less than or equal to

# Logical operators
x = True
y = False

print("\nLogical Operators:")
print(f"x and y: {x and y}")  # Logical AND
print(f"x or y: {x or y}")  # Logical OR
print(f"not x: {not x}")  # Logical NOT

# Bitwise operators
c = 5  # 0101 in binary
d = 3  # 0011 in binary

print("\nBitwise Operators:")
print(f"c & d: {c & d}")  # Bitwise AND
print(f"c | d: {c | d}")  # Bitwise OR
print(f"c ^ d: {c ^ d}")  # Bitwise XOR
print(f"~c: {~c}")  # Bitwise NOT
print(f"c << 1: {c << 1}")  # Bitwise left shift
print(f"c >> 1: {c >> 1}")  # Bitwise right shift

# Assignment operators
e = 10

print("\nAssignment Operators:")
e += 5
print(f"e += 5: {e}")  # e = e + 5
e -= 3
print(f"e -= 3: {e}")  # e = e - 3
e *= 2
print(f"e *= 2: {e}")  # e = e * 2
e /= 4
print(f"e /= 4: {e}")  # e = e / 4
e %= 3
print(f"e %= 3: {e}")  # e = e % 3
e **= 2
print(f"e **= 2: {e}")  # e = e ** 2
e //= 2
print(f"e //= 2: {e}")  # e = e // 2
# Example 1: Basic If-Else Statements

x = 10
y = 20

if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

a = 5
b = 5

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

num = 15

if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# Example 2: Nested If Statements

x = 10
y = 20
z = 30

if x < y:
    if y < z:
        print("x is less than y and y is less than z")
    else:
        print("x is less than y but y is not less than z")
else:
    print("x is not less than y")

age = 18

if age >= 18:
    if age < 65:
        print("You are an adult but not a senior")
    else:
        print("You are a senior")
else:
    print("You are a minor")

# Example 3: Using Logical Operators

x = 10
y = 20

if x < y and y < 30:
    print("x is less than y and y is less than 30")
else:
    print("Condition not met")

num = 15

if not num % 2 == 0:
    print("num is odd")
else:
    print("num is even")

age = 18
has_permission = True

if age >= 18 and has_permission:
    print("You are allowed to enter")
else:
    print("You are not allowed to enter")
# Example 4: Complex Conditions

x = 10
y = 20
z = 30

if x < y and y < z:
    print("x is less than y and y is less than z")
elif x < y and y >= z:
    print("x is less than y but y is not less than z")
elif x >= y and y < z:
    print("x is not less than y but y is less than z")
else:
    print("x is not less than y and y is not less than z")

score = 75
extra_credit = 10

if score + extra_credit >= 90:
    print("Grade: A")
elif score + extra_credit >= 80:
    print("Grade: B")
elif score + extra_credit >= 70:
    print("Grade: C")
elif score + extra_credit >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Example 9: Checking for Leap Year and Number Range

# Leap year check
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Number range check
number = 45

if number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is zero")
elif number > 0 and number <= 50:
    print("The number is between 1 and 50")
else:
    print("The number is greater than 50")

# Temperature check
temperature = 25

if temperature > 30:
    print("It's hot outside")
elif temperature < 10:
    print("It's cold outside")
else:
    print("The weather is moderate")

# Day of the week check
day = "Wednesday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("It's a weekday")
# Example 11: Demonstrating Loops

# For loop
print("For Loop:")
for i in range(5):
    print(f"Iteration {i}")

# While loop
print("\nWhile Loop:")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Nested loops
print("\nNested Loops:")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Loop with break
print("\nLoop with Break:")
for i in range(5):
    if i == 3:
        break
    print(f"Iteration {i}")

# Loop with continue
print("\nLoop with Continue:")
for i in range(5):
    if i == 3:
        continue
    print(f"Iteration {i}")

# Loop with else
print("\nLoop with Else:")
for i in range(5):
    print(f"Iteration {i}")
else:
    print("Loop completed without break")
# Example 12: Printing a Pattern with Loops

# Printing a right-angled triangle pattern
print("Right-angled Triangle Pattern:")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Printing a pyramid pattern
print("\nPyramid Pattern:")
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Printing a diamond pattern
print("\nDiamond Pattern:")
rows = 5
# Upper part of diamond
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
# Lower part of diamond
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    # Example 13: Printing Even and Odd Numbers with Loops

# Printing even numbers from 1 to 10
print("Even Numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Printing odd numbers from 1 to 10
print("\nOdd Numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
# Example 14: Printing a Multiplication Table with Loops

# Printing multiplication table for a given number
number = 5
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Printing multiplication tables from 1 to 10
print("\nMultiplication Tables from 1 to 10:")
for num in range(1, 11):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
# Example 15: Built-in Functions for Lists

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Using built-in functions
print("List Functions:")
print(f"Length of list: {len(my_list)}")
print(f"Maximum value: {max(my_list)}")
print(f"Minimum value: {min(my_list)}")
print(f"Sum of elements: {sum(my_list)}")
print(f"Sorted list: {sorted(my_list)}")
print(f"Reversed list: {list(reversed(my_list))}")
# Example 16: Built-in Functions for Tuples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Using built-in functions
print("\nTuple Functions:")
print(f"Length of tuple: {len(my_tuple)}")
print(f"Maximum value: {max(my_tuple)}")
print(f"Minimum value: {min(my_tuple)}")
print(f"Sum of elements: {sum(my_tuple)}")
print(f"Sorted tuple: {sorted(my_tuple)}")
print(f"Reversed tuple: {tuple(reversed(my_tuple))}")
# Example 17: Built-in Functions for Sets

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Using built-in functions
print("\nSet Functions:")
print(f"Length of set: {len(my_set)}")
print(f"Maximum value: {max(my_set)}")
print(f"Minimum value: {min(my_set)}")
print(f"Sum of elements: {sum(my_set)}")
print(f"Sorted set: {sorted(my_set)}")
# Example 18: Built-in Functions for Dictionaries

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Using built-in functions
print("\nDictionary Functions:")
print(f"Length of dictionary: {len(my_dict)}")
print(f"Keys: {list(my_dict.keys())}")
print(f"Values: {list(my_dict.values())}")
print(f"Items: {list(my_dict.items())}")
print(f"Get value for key 'c': {my_dict.get('c')}")
print(f"Check if key 'a' exists: {'a' in my_dict}")
# Example 19: Demonstrating Functions

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

# Function to find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Using the functions
num1 = 10
num2 = 5

print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")
print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
print(f"Division of {num1} and {num2}: {divide(num1, num2)}")

number = 5
print(f"Factorial of {number}: {factorial(number)}")
# Example 20: Calculating Factorial

# Iterative method to calculate factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive method to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
# Generating Fibonacci Series

# Iterative method to generate Fibonacci series
def fibonacci_iterative(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Recursive method to generate Fibonacci series
def fibonacci_recursive(n, fib_series=[0, 1]):
    if len(fib_series) >= n:
        return fib_series[:n]
    fib_series.append(fib_series[-1] + fib_series[-2])
    return fibonacci_recursive(n, fib_series)

# Input number
number = 10

# Generating Fibonacci series using iterative method
iterative_fib = fibonacci_iterative(number)
print(f"Fibonacci series (iterative) up to {number} terms: {iterative_fib}")

# Generating Fibonacci series using recursive method
recursive_fib = fibonacci_recursive(number)
print(f"Fibonacci series (recursive) up to {number} terms: {recursive_fib}")

# Input number
number = 5

# Calculating factorial using iterative method
iterative_result = factorial_iterative(number)
print(f"Factorial of {number} (iterative): {iterative_result}")

# Calculating factorial using recursive method
recursive_result = factorial_recursive(number)
print(f"Factorial of {number} (recursive): {recursive_result}")


# Lambda function to add two numbers
add = lambda a, b: a + b
print(f"Addition using lambda: {add(10, 5)}")

# Lambda function to find the square of a number
square = lambda x: x ** 2
print(f"Square using lambda: {square(4)}")

# Function with default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# Function with variable-length arguments (*args)
def sum_all(*args):
    return sum(args)

print(f"Sum of all arguments: {sum_all(1, 2, 3, 4, 5)}")

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# Function with both *args and **kwargs
def mixed_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_function(1, 2, 3, 4, 5, name="Alice", age=25)