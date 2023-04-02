#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    a_or_p = s[-2:]
    time = tuple(s[:-2].split(":"))
    if a_or_p == "AM" and time[0] == "12":
        return ":".join(("00",)+time[1:])
    if a_or_p == "PM" and int(time[0]) in range(1,12):
        hour = int(time[0])
        return ":".join((f"{hour+12:02d}",)+time[1:])
    return ":".join(time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
