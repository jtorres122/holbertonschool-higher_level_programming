#!/usr/bin/python3
'''

Module contains a matrix divinding function

'''


def matrix_divided(matrix, div):
    ''' Function divides all elements of a matrix '''

    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"

    if type(matrix) is not list:
        raise TypeError(list_error)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_error)
        if len(matrix[0]) != len(row):
            raise TypeError(len_error)
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda fun: round(fun / div, 2), ele)) for ele in matrix]
