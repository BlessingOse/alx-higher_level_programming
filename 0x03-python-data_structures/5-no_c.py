#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    p = 0

    new_string = my_string[:]

    for x in range(length):
        if (my_string[x] == 'c' or my_string[x] == 'C'):
            new_string = new_string[:(x - p)] + my_string[(x + 1):]
            p = p + 1

    return (new_string)
