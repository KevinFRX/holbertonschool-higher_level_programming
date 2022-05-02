#!/usr/bin/python3
def max_integer(my_list=[]):
    j = my_list[0]
    if not my_list:
        return
    for i in my_list:
        if j < i:
            j = i
    return j
