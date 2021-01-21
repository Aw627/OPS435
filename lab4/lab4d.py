#!/usr/bin/env python3

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(ff):
    a = (ff[0:5])
    return a

def last_seven(ls):
    a = (ls[-7:])
    return a

def middle_number(mn):
    a = str(mn)
    done = a[1:3]
    return done

def first_three_last_three(ft, lt):
    b = ft[0:3]
    c = lt[-3:]
    bc = b + c
    return bc

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

