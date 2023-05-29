#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for p in range(x):
        try:
            print("{}".format(my_list[p]), end='')
        except:
            break
        else:
            count = count + 1

    print()
    return (count)
