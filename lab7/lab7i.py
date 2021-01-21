#!/usr/bin/env python3
# Student ID: hcawong
def function1():
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:',schoolName)
function1()
schoolName = 'SICT'
print('print() in main on schoolName:',schoolName)
function2()
print('print() in main on schoolName:',schoolName)
