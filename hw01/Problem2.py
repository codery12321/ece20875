#!/usr/bin/python3
import math
import sys
n = 21
# Your code should be below this line

if(n>31):
    sys.exit("not valid")
check = n%7
if(check != 1) and (check != 2):
    print("Weekday")
else:
    print("Weekend")
