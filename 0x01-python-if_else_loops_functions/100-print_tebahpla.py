#!/usr/bin/python3
j = 121
for i in range(122, 96, -2):
    print(f"{chr(i)}{chr(j).upper()}", end='')
    j -= 2
