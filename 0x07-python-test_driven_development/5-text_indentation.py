#!/usr/bin/python3
"""Module to indent a text"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    or returns a TypeError if text if not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    aux = ""
    flag = 0
    for i in text:
        if flag == 0:
            aux += i
        else:
            flag = 0
        if i in chars:
            aux += "\n\n"
            flag = 1
    print(aux, end="")
