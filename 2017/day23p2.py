#!/usr/bin/env python

import sys

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True


N, stepsize = 125100, 17

h = 0
for b in range(N - 17000, N+stepsize, stepsize):

    if not isPrime2(b):
        h += 1

print "answer (part 2):", h
sys.exit()


# this is the machine code in high level - VERY SLOW!
for b in range(N - 17000, N+17, 17):

    flag = True
    for d in xrange(2, b):
        for e in xrange(2, b):
            if d * e == b:
                flag = False

    if not flag:
        h += 1
print h
