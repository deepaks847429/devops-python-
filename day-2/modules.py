# modules in python
# Importing a module
# example of using modules in python
# import modules
# modules.greet()
# print(modules.greeting)

# writing a module to show use casee in python
def greet():
    print("Hello, welcome to Python modules!")
greeting = "This is a greeting from the module."
# This module can be saved as modules.py and imported in other scripts.
# Importing specific functions or variables from a module
from modules import greet, greeting
greet()
print(greeting)

# lambda functions
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# Example of a lambda function
add = lambda x, y: x + y
print("Sum using lambda function:", add(5, 3))
# Using lambda functions with map, filter, and reduce
from functools import reduce  
# Using map to apply a function to all items in an iterable
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map:", squared_numbers)  
# Using filter to filter items in an iterable
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)
# Using reduce to apply a function cumulatively to the items of an iterable 
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers using reduce:", sum_of_numbers)
# Using lambda functions in sorting
# Sorting a list of tuples based on the second element
tuples_list = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print("Sorted tuples by second element:", sorted_tuples)
# Using lambda functions in sorting
# Sorting a list of dictionaries based on a specific key
dicts_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_dicts = sorted(dicts_list, key=lambda x: x['age'])
print("Sorted dictionaries by age:", sorted_dicts)
# Using lambda functions in sorting
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
  return True
# Example usage of the is_prime function    
print("Is 7 prime?", is_prime(7))  # Output: True
print("Is 10 prime?", is_prime(10))  # Output: False

      
 
