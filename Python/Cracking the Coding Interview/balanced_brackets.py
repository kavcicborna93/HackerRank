#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        stack = []
        expression = input()
        length = len(expression)
        if length % 2 != 0 or length == 0:
            print(False)
        else:
            dictionary = {'{':'}','[':']','(':')'}
            for bracket in expression:
                if bracket in dictionary.keys():
                    stack.append(bracket)
                elif bracket in dictionary.values():
                    if len(stack) == 0 or dictionary[stack[-1]] != bracket:
                        print('NO')
                        break
                    else:
                        stack.pop()
            else:
                if len(stack) == 0:
                    print('YES')
                else:
                    print('NO')
