#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    p = len(sys.argv) - 1

    if p == 0:
        print("{} arguments.".format(p))
    elif p == 1:
        print("{} argument:".format(p))
    else:
        print("{} arguments:".format(p))

    if p >= 1:
        p = 0
        for arg in sys.argv:
            if p != 0:
                print("{}: {}".format(p, arg))
            p = p + 1
