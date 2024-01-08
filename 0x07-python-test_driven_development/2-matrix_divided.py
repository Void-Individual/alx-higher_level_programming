#!/usr/bin/python3
"""Module to divide a matrix"""


def matrix_divided(matrix, div):
    """Function to divide a matrix

    Args;
    matrix: the matrix to be divided
    div: number (int or float) to be divided

    Return: a new matrix with divided elements

    Raise: TypeError if any of the values isn't an int or float
    - ZEroDivisionError if div is 0
    """

    new = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for lis in matrix:
        if len(lis) != len(matrix[0]):
            raise TypeError("Each row of the matrix must"
                            " have the same size")
        new_row = []
        for el in lis:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_row.append(round((el / div), 2))
        new.append(new_row)
    return new
