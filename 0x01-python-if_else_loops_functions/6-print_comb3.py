#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i != j and i < j and i != 8:
            print(f"{i}{j},", end=' ')
        elif i != j and i < j:
            print(f"{i}{j}")
