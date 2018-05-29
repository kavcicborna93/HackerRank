#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())
        if n == 1:
            print('Not prime')
        else:
            for divisors in range (2,int(math.sqrt(n))+1):
                if n % divisors == 0:
                    print('Not prime')
                    break
            else:
                print('Prime')
