#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    alt = 0
    valys = 0
    down = False
    for i in path:
        if i == 'U':
            alt += 1
            if down and alt == 0:
                valys += 1
                down = False
        else:
            alt -= 1
            if alt < 0:
                down = True
    
    return valys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
