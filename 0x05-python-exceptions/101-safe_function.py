#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        r = None
    return r
