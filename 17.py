#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    l = len(arr)
    print(
        f"{len([_ for _ in arr if _>0])/l:.6f}",
        f"{len([_ for _ in arr if _<0])/l:.6f}",
        f"{len([_ for _ in arr if _==0])/l:.6f}",        
        sep="\n"
    )

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
