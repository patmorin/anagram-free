#!/usr/bin/python3


A = [2,1,3,1,5,3,1,4,1,5,1,4,1,2]
A = [x - 1 for x in A]
seqs = [A]
for i in range(4):
    seqs.append([(x+1)%5 for x in seqs[i]])

def make_sequence(k):
    if k == 0: return list([1])
    s = make_sequence(k-1)
    s2 = list()
    for i in s:
        s2.extend(seqs[i])
    return s2

def print_sequence(s):
    for x in s:
        print(" ".join([str(x+6) for x in s]))

s = make_sequence(2)
print_sequence(s)

import matplotlib.pyplot as plt

counters = [list([0]) for _ in range(5)]
"""
for x in s:
    for i in range(len(counters)):
        counters[i].append(counters[i][-1] + (x==i))
"""
k = 10
for x in s[:k//2]:
    counters[x][0] -= 1
for x in s[k//2:k]:
    counters[x][0] += 1

print(counters)

for j in range(len(s)-k):
    for i in range(len(counters)):
        counters[i].append(counters[i][-1])
    counters[s[j]][-1] += 1
    counters[s[j+k]][-1] += 1
    counters[s[j+k//2]][-1] -= 2

for i in range(len(counters)):
    plt.plot(counters[i], label=['a','b','c','d','e'][i])

plt.show()
"""
for i in range(5):
    ell = list(0)
    accumulators.append(ell)
    for x in s:

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
"""
