#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    sentence = list(sentence)
    for i in range(1, len(sentence)):
        x, y = sentence[i].lower(), sentence[i-1].lower()        
        if x==y or " " in [x, y]: continue
        print(x, y)
        sentence[i] = x.lower() if x<y else x.upper()
        print(x<y, "{}: {}".format(x, ord(x)), "{}: {}".format(y, ord(y)))
    return ''.join(sentence)
    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
