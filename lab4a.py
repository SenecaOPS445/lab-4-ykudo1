#!/usr/bin/env python3
#Authorid: ykudo


def join_sets(s1, s2):
    # join_sets will return a set that contains every value from both s1 and s2
    join_1 = s1.union(s2)
    
    return join_1

def match_sets(s1, s2):
    # match_sets will return a set that contains all values found in both s1 and s2
   inter_1 = s1.intersection(s2)
   #inter_2 = set2.intersection(set1)
   #inter_res = str(inter_1) + str(inter_2)
   #return inter_res
   return inter_1

def diff_sets(s1, s2):
    # diff_sets will return a set that contains all different values which are not shared between the sets
    diff_1 = s1.symmetric_difference(s2)
    #diff_2 = set2.symmetric_difference(set1)
    #diff_res = str(diff_1) + str(diff_2)
    #return diff_res
    return diff_1

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
