#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for p in range(x):
        try:
            print("{:d}".format(my_list[p]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count = count + 1

    print()
    return (count)
