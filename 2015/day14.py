#!/usr/bin/env python

import numpy as np

def distance(reindeer, tmax):
    speed, len_fly, len_rest, _ = reindeer

    t, d = 0, 0
    while t < tmax:
        if tmax - t > len_fly:
            d += speed * len_fly
            t += len_fly
        else:
            d += speed * (tmax - t)
            return d
        if tmax - t > len_rest:
            t += len_rest
        else:
            return d

# read data into structure
data = [line.rstrip('\n') for line in open('day14.in')]
reindeer = np.zeros((len(data), 4))
for i, d in enumerate(data):
    words = d.split(' ')
    speed, len_fly, len_rest = int(words[3]), int(words[6]), int(words[-2])
    reindeer[i, 0:3] = speed, len_fly, len_rest

# simulate race
tmax = 2503
for t in xrange(1, tmax+1):
    # find distances at time t
    dists = [distance(reindeer[i, :], t) for i in xrange(len(reindeer))]
    # select winner(s) and add points to their count
    winners = np.argwhere(dists == np.amax(dists))
    reindeer[winners, -1] += 1

print "part a:", int(np.max(dists))
print "part b:", int(np.max(reindeer[:, -1]))
