#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mn, mx = sum(arr), 0
    for i in list(combinations(arr, 4)):
        s = sum(i)
        if s>mx: mx=s
        if s<mn: mn=s
        
    print(mn, mx)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
