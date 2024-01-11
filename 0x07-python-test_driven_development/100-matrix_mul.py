#!/usr/bin/python3
"""Module to multiply lists"""


def matrix_mul(m_a, m_b):
    """A function to multiply lists

    Args:
    m_a - must be a list of lists of ints or floats
    m_a - must be a list of lists of ints or floats

    Raise:
    - TypeError if m_a or m_b isnt a list or if they
    don't contain only floats or ints or if the contained
     lists aren't the same size
    - ValueError if m_a or m_b is empty or if they can't
    be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for lis in m_a:
        if not isinstance(lis, list):
            raise TypeError("m_a must be a list "
                            "of lists")
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
        if len(lis) != len(m_a[0]):
            raise TypeError("each row of m_a must be "
                            "of the same size")
        for el in lis:
            if not isinstance(el, (int, float)):
                raise TypeError("m_a should contain "
                                "only integers or floats")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for lis in m_b:
        if not isinstance(lis, list):
            raise TypeError("m_b must be a list "
                            "of lists")
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
        if len(lis) != len(m_b[0]):
            raise TypeError("each row of m_b must be "
                            "of the same size")
        for el in lis:
            if not isinstance(el, (int, float)):
                raise TypeError("m_b should contain "
                                "only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for row_a in m_a:
        new_row = []
        for col_b in range(len(m_b[0])):
            value = 0
            for i in range(len(m_a[0])):
                value += row_a[i] * m_b[i][col_b]
            new_row.append(int(value))
        matrix.append(new_row)
    return matrix
