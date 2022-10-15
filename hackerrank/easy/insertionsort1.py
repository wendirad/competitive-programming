#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    last_element = arr[-1]
    for i in range(n):
        if i == (n - 1) or arr[-(i + 2)] <= last_element:
            arr[-(i + 1)] = last_element
            print(*arr)
            break
        arr[-(i + 1)] = arr[-(i + 2)]
        print(*arr)
            
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
