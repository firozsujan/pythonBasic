
# Task # HackerRank
# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    charArray = []
    charArray = s.split(' ')
    
    updatedString = ""
    
    for i in charArray:
        newWord =""
        if len(i)>0:
            firstChar = i[0]
            upper = i[0].upper()
            newWord = i.replace(firstChar, upper, 1)
        updatedString = updatedString + newWord + " "
    
    return updatedString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
