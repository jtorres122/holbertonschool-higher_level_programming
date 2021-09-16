#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []

    for i in matrix:
        for x in i:
            y = x ** 2
            new_matrix.append(y)

    return (new_matrix)
