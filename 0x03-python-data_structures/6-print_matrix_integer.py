#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        print(' '.join(format(row)for row in i))
