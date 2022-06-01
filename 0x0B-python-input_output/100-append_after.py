#!/usr/bin/python3
"""Module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after
    each line containing a specific string (see example)
    """
    with open(filename, encoding="utf-8") as f:
        file_content = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        text = ""
        for line in file_content:
            text += line
            if search_string in line:
                text += new_string
        f.write(text)
