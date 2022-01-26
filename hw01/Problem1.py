#!/usr/bin/python3
import math
number = 100

# Your code should be below this line
numpos4 = 5*number*number+4
numneg4 = 5*number*number-4
def isPerfectSquare(number):
    x = int(math.sqrt(number))
    return x*x == number


if (isPerfectSquare(numpos4)) or (isPerfectSquare(numneg4)):
    if (number%2 == 0) and (number>0):
        print("Yes")
    else:
        print("No")
else:
    print("No")
