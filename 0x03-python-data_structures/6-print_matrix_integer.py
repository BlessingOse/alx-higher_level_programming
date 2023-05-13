#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for p in range(len(matrix[x])):
            if p != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][p]), end='')
        print()
