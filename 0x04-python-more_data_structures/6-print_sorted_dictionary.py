#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    for i, j in sorted_items:
        print(i, end="")
        print(":", j)
