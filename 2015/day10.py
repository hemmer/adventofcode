#!/usr/bin/env python

import itertools as it


def increaseInput(ii):
    freqs = [[k,len(list(g))] for k, g in it.groupby(str(ii))]
    return ''.join([str(f[1]) + f[0] for f in freqs])


ii = 1321131112
for i in xrange(40):
    ii = increaseInput(ii)

print 'part a:', len(ii)

ii = 1321131112
for i in xrange(50):
    ii = increaseInput(ii)

print 'part b:', len(ii)
