#!/usr/bin/python3
def uniq_add(my_list=[]):
    conjunto = set(my_list)
    res = 0
    for i in conjunto:
        res += i
    return res
