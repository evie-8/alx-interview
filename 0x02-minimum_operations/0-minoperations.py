#!/usr/bin/python3
"""
    m   in operations to copy and paste letters function
"""


def minOperations(n):
    op = 0
    minop = 2
    while n > 1:
        while n % minop == 0:
            op += minop
            n /= minop
        minop += 1
    return op
