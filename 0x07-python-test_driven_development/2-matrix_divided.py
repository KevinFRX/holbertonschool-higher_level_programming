#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Funtion that returns a new matrix divided by div,
    a TypeError if matrix is not a matrix of integers/floats,
    a TypeError if the rows of the matrix do not have the same size
    a TypeError if div is not a number
    or a ZeroDivisionError if div is 0
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    size = -1
    for row in matrix:
        if len(row) != size and size != -1:
            raise TypeError("Each row of the matrix must have the same size")
        size = len(row)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
