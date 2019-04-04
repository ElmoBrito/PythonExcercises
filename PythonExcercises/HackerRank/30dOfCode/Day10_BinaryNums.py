"""Task 
Given a base- integer, , convert it to binary (base-).
Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def n_to_bin(n):
    if 1 <= n and n <= 10**6:
        consec_one = len(max(bin(n)[2:].split("0")))
        return consec_one

if __name__ == '__main__':
    n = int(input())
    print(n_to_bin(n))
