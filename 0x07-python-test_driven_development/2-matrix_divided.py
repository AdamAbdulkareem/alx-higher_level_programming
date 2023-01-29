#!/usr/bin/python3
"""Division module
Args:
    param1 (list): The first parameter
    param2 (int): The second parameter
"""


def matrix_divided(matrix, div):
    """A function that divides the elements in a list by param2
    Returns: A list element that is divided by param2
    """
    list_index1 = []
    if not all(i == 3 for i in map(len, matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for index_1 in matrix:
        list_index2 = []
        for index_2 in index_1:
            if type(index_2) == int or type(index_2) == float:
                division = index_2 / div
                two_dp = round(division, 2)
                list_index2.append(two_dp)
            else:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
        list_index1.append(list_index2)
    return list_index1
