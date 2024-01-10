#!/usr/bin/python3
"""Module to emulate Pascal's triangle"""


def pascal_triangle(n):
    """Function to return a list with triangle
    of size n"""

    if n <= 0:
        return []

    triangle = []
    prev = []

    for x in range(n):
        n_triangle = []
        c1 = -1
        c2 = 0
        for y in range(len(prev) + 1):
            if c1 == -1 or c2 == len(prev):
                n_triangle += [1]
            else:
                n_triangle += [prev[c1] + prev[c2]]
            c1 += 1
            c2 += 1
        triangle.append(n_triangle)
        prev = n_triangle[:]

    return triangle
