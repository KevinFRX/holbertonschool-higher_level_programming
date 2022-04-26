#!/usr/bin/python3
j = 98
for i in range(97, 122, 2):
    print(f"{chr(i).upper()}{chr(j)}", end='')
    j += 2
