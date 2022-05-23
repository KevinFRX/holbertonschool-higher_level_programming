#!/usr/bin/python3
"""Module to multiply matrixes"""


def matrix_mul(m_a, m_b):
    """
    Function that returns a new matrix with the result of the multiplication,
    a TypeError if m_a or m_b are not lists,
    a TypeError if m_a or m_b are not lists of lists,
    a ValueError if m_a or m_b are empty,
    a TypeError if m_a or m_b contains non-numbers,
    a TypeError if m_a or m_b are not rectangles
    or a ValueError if m_a and m_b can`t be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    lena = None
    for i in m_a:
        if lena is None:
            lena = len(i)
            if lena == 0:
                raise ValueError("m_a can't be empty")
        if lena != len(i):
            raise TypeError("each row of m_a must be of the same size")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for j in m_b:
        if not isinstance(j, list):
            raise TypeError("m_b must be a list of lists")
    lenb = None
    for j in m_b:
        if lenb is None:
            lenb = len(j)
            if lenb == 0:
                raise ValueError("m_b can't be empty")
        if lenb != len(j):
            raise TypeError("each row of m_b must be of the same size")
    for i in m_a:
        for ii in i:
            if not isinstance(ii, int) and not isinstance(ii, float):
                raise TypeError("m_a should contain only integers or floats")
    for j in m_b:
        for jj in j:
            if not isinstance(jj, int) and not isinstance(jj, float):
                raise TypeError("m_b should contain only integers or floats")
    if lena != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m = []
    for i in range(len(m_a)):
        r = []
        for j in range(lenb):
            n = 0
            for k in range(lena):
                n += m_a[i][k] * m_b[k][j]
            r.append(n)
        m.append(r)
    return m
