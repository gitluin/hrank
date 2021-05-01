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
    elev = 0
    valleys = 0
    
    for char in path:
        old_elev = elev
        
        if (char == 'D'):
            elev = elev - 1
        elif (char == 'U'):
            elev = elev + 1
            
        if (old_elev == 0 and elev < old_elev):
            valleys = valleys + 1
            
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
