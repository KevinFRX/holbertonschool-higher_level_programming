#!/usr/bin/python3
def max_integer(my_list=[]):
    j = 0
    if my_list:
        for i in my_list:
            if j < i:
                j = i
        return j
    return None
