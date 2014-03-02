#!/usr/bin/env python

# Find PI to the Nth Digit - Enter a number and have the program generate PI up
# to that many decimal places. Keep a limit to how far the program will go.

import math
from decimal import *

MY_PROMPT = lambda: raw_input("> ")
error = "Please try again with a positive number, less than 48"
message = ("Enter a number from 1 to 48 to see Pi to that many places,"
           " or q to quit.")


def get_input(prompt_func):
    print message
    prec = prompt_func()
    return prec


def pi(prec):
    if prec > 48:
        return error
    try:
        getcontext().prec = int(prec) + 1
        pi = Decimal(math.pi).quantize(
            Decimal('.{}'.format('0' * prec)), rounding=ROUND_DOWN
        )
        return pi
    except Exception:
        return error


def main(prompt=MY_PROMPT, prompt2=None):
    """
    Returns the number Pi, rounded down, to the number of places given as
    input, up to 48 places.
    """
    control = lambda: get_input(prompt2) if prompt2 else get_input(prompt)
    prec = get_input(prompt)
    while prec != 'q':
        try:
            prec = int(prec)
        except ValueError:
            print error
            prec = control()
            continue

        if prec > 48:
            print error
            prec = control()
            continue

        print pi(prec)
        prec = control()

    print "Goodbye."
    exit(0)

if __name__ == "__main__":
    main()
