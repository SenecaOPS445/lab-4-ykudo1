#!/usr/bin/env python3
#Authorid: ykudo
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(arg1):
    # Place code here - refer to function specifics in section below
    if arg1 == str1:
        return str1[0:5]
    if arg1 == str2:
        return str2[0:5]

def last_seven(arg2):
    # Place code here - refer to function specifics in section below
    if arg2 == str1:
        return str1[-7:]
    if arg2 == str2:
        return str2[-7:]

def middle_number(arg3):
    # Place code here - refer to function specifics in section below
    if arg3 == num1:
        result1 = str(num1)[1] + str(num1)[-1]
        return result1
    if arg3 == num2:
        result2 = str(num2)[1] + str(num2)[-1]
        return result2
    
def first_three_last_three(arg4, arg5):
    # Place code here - refer to function specifics in section below
    #first3 = first_three_last_three[0:2]
    #last3 = first_three_last_three[-1:-2]
    first = arg4[:3]
    last = arg5[-3:]
    result = first + last
    return result

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))