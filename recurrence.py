#!/usr/bin/python3

import sys
from math import log
from fractions import Fraction


memo = dict()
one_half = Fraction(1,2)
three_eighths = Fraction(3, 8)

def recurrence(h, k):
    global memo
    if k == 0 or h == 0: return 0
    # print(memo)
    if (h,k) in memo: return memo[(h,k)]
    p =  1/h + ((h-1)/h)*(1/2)*(recurrence(h-1, k)+recurrence(h-1,k-1))
    memo[(h,k)] = p
    return p

def recurrence2(h, w, r):
    global memo
    if h == 0: return 0
    if (h, w, r) in memo: return memo[(h, w, r)]
    if (w >= three_eighths):
        res = ((h-1)/(2*h))*recurrence2(h-1, 2*w-one_half, r)
    elif (w <= 1/r):
        res = 0
    else:
        res = 1/h + ((h-1)/(2*h))*(recurrence2(h-1, 4*w/3, r)
                                   +recurrence2(h-1, 2*w/3, r))
    memo[(h, w, r)] = res
    return res

if __name__ == "__main__":
    r = Fraction(20)
    w = Fraction(1,4)
    for h in range(1000):
        k = int(log(2**h, 3))
        result = recurrence2(Fraction(h), w, r)
        result_f = result.numerator / result.denominator
        print("{} {} {} {} {}".format(h, w, r, result_f, result))
        sys.stdout.flush()
