#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if len(matrix) <= 0:
        return

    for i in matrix:
        print(' '.join("{:d}".format(row)for row in i))
