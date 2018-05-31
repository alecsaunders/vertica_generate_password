#!/usr/bin/env python

import string
import random

def main():
    N = 12
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    digits = '1234567890'
    symbols = '!#$*%@()[].,?'

    hash = ''.join(random.choices(upper_case + lower_case + digits + symbols, k=N))
    print(hash)

if __name__ == '__main__':
    main()
