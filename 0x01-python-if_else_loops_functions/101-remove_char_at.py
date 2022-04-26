#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = "\0"
    for i in range(len(str)):
        if i != n:
            cpy = cpy + str[i]
        return (cpy)
