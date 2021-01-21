#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID:hcawong

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    sum_number = int(number1) + int(number2)
    return sum_number
def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    sub_number = int(number1) - int(number2)
    return sub_number
    
def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    mul_number = int(number1) * int(number2)
    return mul_number


if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))

