#!/usr/bin/env python3
# Author ID: ykudo

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    
    count = 0
    length = len(sobj)
    while count < length:
        for i in sobj:
            if i in '0123456789':
                continue
            elif i in 'abcdefghijklmnopqrstuvwxyz':
                return False
            elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return False
            count = count + 1
        return True
    
    #for i in sobj:
    #    if i in '0123456789':
    #        return True
    #    else:
    #        return False

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')