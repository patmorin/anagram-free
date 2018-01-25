#!/usr/bin/python3

from collections import defaultdict
from itertools import product
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

    # Fill the bottom row (h = 0)
    for a, b in product(range(r+1), range(r+1)):
        t[0,1,a,b] = 0
    for a, b in product(range(1, r+1), range(1, r+1)):
        t[0,0,a,b] = 0

    for h in range(1,h0+1):
        # print_t(t, [h-1], [0], [0,1,2], [0,1,2])
        for w, a, b in product(range(2**h + 1), range(r+1), range(r+1)):
            best = -inf
            for w0 in range(w+1):
                w1 = w - w0
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

    """
    for w in range(2**h+1):
        if t[(h,w,r,r)] >= 0:
            string = make_string(s, h, w, r, r)
            print("{} (w={} v={})".format(string, w, t[h,w,r,r]))
    """
    q = [t[h,w,r,r] for w in range(2**h)]
    wmax = imax(q)
    string = make_string(s, h, wmax, r, r, r)
    print("{} (w={} v={})".format(string, wmax, t[h,wmax,r,r]))
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
    """
    try:
        h = int(sys.argv[1])
        r = int(sys.argv[2])
    except:
        sys.stderr.write("Usage: {} <h> <r>\n".format(sys.argv[0]))
        sys.exit(-1)
    val = optimal(h, r)
    print(h, r, val, val/(h*2**h))
    """
    for h in range(2, 20):
       print(h, optimal(h, 5)/(h*2**(h+1)))
