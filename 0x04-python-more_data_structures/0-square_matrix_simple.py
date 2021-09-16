#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []
    for row in matrix:
        new = []
        for col in row:
            y = col ** 2
            new.append(y)
        new_matrix.append(new)

    return (new_matrix)
