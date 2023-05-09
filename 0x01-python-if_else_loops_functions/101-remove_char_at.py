#!/usr/bin/python3
def remove_char_at(str, n):
    x = ""
    for p in range(len(str)):
        if p != n:
            x = x + str[p]
    return (x)
