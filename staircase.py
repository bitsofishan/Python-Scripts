"""#
##
###
####

Input Format
A single integer, , denoting the size of the staircase.
Output Format
Print a staircase of size using # symbols and spaces.
Note: The last line must have spaces in it.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
 
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
