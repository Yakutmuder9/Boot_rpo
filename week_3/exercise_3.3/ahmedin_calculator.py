""" 
    Title: ahmedin_myworld.py
    Author: Professor Krasso
    Date: 02 April 2023
    Modified By: Yakut Ahmedin
    Description: Exercise 3.3 – Python Variables and Functions.
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

# variables for testing
num1 = 8
num2 = 5

# test each function with the testing variables
add_result = add(num1, num2)
subtract_result = subtract(num1, num2)
divide_result = divide(num1, num2)
multiply_result = multiply(num1, num2)

# Building the result strings 
add_str = "{} + {} is {}.".format(num1, num2, add_result)
subtract_str = "{} - {} is {}.".format(num1, num2, subtract_result)
divide_str = "{} / {} is {}.".format(num1, num2, divide_result)
multiply_str = "{} * {} is {}.".format(num1, num2, multiply_result)

# Printing the results
print(add_str)
print(subtract_str)
print(divide_str)
print(multiply_str)