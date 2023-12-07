#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cnt = len(matrix)
    new = []
    for c1 in range(cnt):
        x = matrix[c1]
        temp = []
        for y in x:
            temp.append(y * y)
        new.append(temp)
    return new
