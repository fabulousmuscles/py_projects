# Find PI to the Nth Digit - Enter a number and have the program generate PI up
# to that many decimal places. Keep a limit to how far the program will go.

import math
from decimal import *

error = "Please try again with a positive number, less than 48"
message = "Enter a number from 1 to 48 to see Pi to that many places."


def get_input(prompt_func):
    print message
    prec = prompt_func()
    return prec


def myprompt():
    return raw_input("> ")


def main(prompt=myprompt, prompt2=myprompt):
    """
    Returns the number Pi, rounded down, to the number of places given as
    input, up to 48 places.
    """
    prec = get_input(prompt)
    while prec != 'q':
        try:
            prec = int(prec)
        except ValueError:
            print error
            prec = get_input(prompt2)
            continue

        if prec > 48:
            print error
            prec = get_input(prompt2)
            continue

        getcontext().prec = prec + 1

        print Decimal(math.pi).quantize(
            Decimal('.{}'.format('0' * prec)), rounding=ROUND_DOWN
        )
        prec = get_input(prompt2)

    print "Goodbye."
    exit(0)

if __name__ == "__main__":
    main()
