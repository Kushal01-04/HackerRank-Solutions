#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

    d = {}

    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    dict01 = sorted(d.items(), key=lambda x: (-x[1], x[0]))

    for key, value in dict01[:3]:
        print(key, value)
    
