#!/usr/bin/python3
"""Module to multiply two matrixes using NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrixes"""
    return numpy.matmul(m_a, m_b)
