#!/usr/bin/python3

from collections import defaultdict
from itertools import product
from math import log
import bisect
import sys


def print_t(t, rh, rw, ra, rb):
    for h, w, a, b in product(rh, rw, ra, rb):
        print("{},{},{},{}={}".format(h, w, a, b, t[h,w,a,b]))

def imax(a):
    m = 0
    for i in range(len(a)):
        if a[i] > a[m]:
            m = i
    return m

""" Find value of optimal solution (a value in 0,...,h*2**h) in a tree
    of height h that has not more than r consecutive zeros. """
def optimal(h, r):
    # t[h,w,a,b] = value of optimal solution of height h using w 1s with
    # at most a leading 0s and at most b trailing 0s.
    h0 = h
    inf = h*2**(h+1)+1

    # a value of -inf signals an invalid string (too dense or too heavy)
    t = defaultdict(lambda: -inf)
    s = defaultdict(lambda: (-1,-1))    # used to reconstruct optimal string

    base = 1.05
    apxvals = [0]+[int(base**i) for i in range(int(log(2**h, base)))]
    apxvals = sorted(set(apxvals))

    # Fill the bottom row (h = 0)
    for a, b in product(range(r+1), range(r+1)):
        t[0,1,a,b] = 0
    for a, b in product(range(1, r+1), range(1, r+1)):
        t[0,0,a,b] = 0

    for h in range(1,h0+1):
        # print_t(t, [h-1], [0], [0,1,2], [0,1,2])
        for w, a, b in product(apxvals, range(r+1), range(r+1)):
            best = -inf
            for w0 in [x for x in apxvals if x <= w+1]:
                w1 = w - w0
                i = bisect.bisect_left(apxvals, w1)
                w1 = apxvals[i]
                bonus = [0,2**h][w0 > 2*w1 or w1 > 2*w0]
                if w0 == 0 and w1 == 0:
                    x = 2**(h-1)
                    this = t[h-1,w0,r,b-x] + t[h-1,w1,a-x,r] + bonus
                elif w0 == 0:
                    x = 2**(h-1)
                    this = t[h-1,w0,a,r] + t[h-1,w1,r-x,b] + bonus
                elif w1 == 0:
                    x = 2**(h-1)
                    this = t[h-1,w0,a,b-x] + t[h-1,w1,r,b] + bonus
                else:
                    for x in range(r+1):
                        this = t[h-1,w0,a,x] + t[h-1,w1,r-x,b] + bonus
                        if this > best:
                            best = this
                            s[h,w,a,b] = w0, w1, x
                if this > best:
                    best = this
                    s[h,w,a,b] = (w0, w1, x)
            t[h,w,a,b] = best

    q = [t[h,w,r,r] for w in apxvals]
    wmax = imax(q)
    #string = make_string(s, h, wmax, r, r, r)
    #print("{} (w={} v={})".format(string, wmax, t[h,wmax,r,r]))
    return q[wmax]

def make_string(s, h, w, r, a, b):
    if h == 0:
        return str(w)
    if w == 0:
        return "0" * 2**h
    if (h,w,a,b) in s:
        w0, w1, x = s[h,w,a,b]
        return make_string(s, h-1, w0, r, a, x) \
               + make_string(s, h-1, w1, r, r-x, b)
    return "?" * 2**h

if __name__ == "__main__":
    try:
        r = int(sys.argv[1])
    except:
        sys.stderr.write("Usage: {} <r>\n".format(sys.argv[0]))
        sys.exit(-1)
    for h in range(1, 100):
        opt = optimal(h, r)
        print(h, opt/(h*2**(h+1)))
        sys.stdout.flush()
