#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    occur = 0
    remain_occur = 0
    
    for char in s:
        if (char == 'a'):
            occur += 1
    
    stop = n % len(s)
        
    if (stop == 0):
        return round(occur * (n / len(s)))
    else:
        for i in range(0,stop):
            if (s[i] == 'a'):
                remain_occur += 1
                
        return (occur * (n // len(s))) + remain_occur

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
