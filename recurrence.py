#!/usr/bin/python3

from math import log
from fractions import Fraction

memo = dict()

def recurrence(h, k):
    global memo
    if k == 0 or h == 0: return 0
    # print(memo)
    if (h,k) in memo: return memo[(h,k)]
    p =  1/h + ((h-1)/h)*(1/2)*(recurrence(h-1, k)+recurrence(h-1,k-1))
    memo[(h,k)] = p
    return p

def recurrence2(h, w):
    if h == 0: return Fraction(0)
    if (h, w) in memo: return memo[(h,w)]
    half = Fraction(1,2)
    if (w >= Fraction(3,8)):
        res = Fraction(h-1,h)*half*recurrence2(h-1, 2*w-half)
    elif (w <= Fraction(1,20)):
        res = Fraction(0)
    else:
        res = Fraction(1,h) + Fraction(h-1,h)*half*(recurrence2(h-1,4*w/3)+recurrence2(h-1,2*w/3))
    memo[(h,w)] = res
    return res

for h in range(100):
    k = int(log(2**h, 3))
    # print("({},{})=>{}".format(h, k, recurrence(h, k)))
    #print("({},{})=>{}".format(h, 5, recurrence(h, 5)))
    result = recurrence2(h, Fraction(1,4))
    result_f = result.numerator / result.denominator
    print("({},{})=>{} ({})".format(h, Fraction(1,4), result_f, result))
