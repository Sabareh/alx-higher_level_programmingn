#!/usr/bin/python3
def square_materix_simple(matrix=[]):
    return ([list(map(lambda x: x * x,row)) for row in matrix])
