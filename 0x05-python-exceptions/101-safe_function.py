#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as p:
        sys.stderr.write("Exception: {}\n".format(p))
        result = None

    return (result)
