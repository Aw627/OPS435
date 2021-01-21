#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID:hcawong

def operate(n1, n2, operator):
    # Place logic in this function

    if operator == 'add':
        add_number = int(n1) + int(n2)
        return add_number 
    elif operator == 'subtract':
        subtract_number = int(n1) - int(n2)
        return subtract_number
    elif operator == 'multiply':
        multiply_number = int(n1) * int(n2)
        return multiply_number
    return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
