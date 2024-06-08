#!/usr/bin/python3
"""
This module defines a function `matrix_divided` that divides all
elements of a matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix with the results rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be an integer or float.

    Returns:
        A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if each row of the matrix is not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check if the matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows in the matrix are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
