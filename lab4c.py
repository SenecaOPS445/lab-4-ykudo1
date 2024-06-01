#!/usr/bin/env python3
#Authorid: ykudo

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    num = [2, 3, 0, 4, 1]
    num_keys = [keys[a] for a in num]
    num_values = [values[b] for b in num]
    
    dict = {}
    count = 0
    while count < 5:
        dict_keys = num_keys[count]
        dict_values = num_values[count]
        dict[dict_keys] = dict_values
        count = count + 1
    return dict
    
    #dict_new = dict(zip(list_keys, list_values))
    #return dict_new


def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below

    inter1 = dict(dict1.items() & dict2.items())
    inter2 = inter1.values()
    return set(inter2)



if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)