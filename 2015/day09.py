#!/usr/bin/env python

import numpy as np
import itertools


data = np.array([line.rstrip('\n').split(' ') for line in open('day09.in')])
cities = list(set(np.append(data[:, 0],data[:, 2])))
num_cities = len(cities)
cities_i = np.arange(num_cities)

dists = np.zeros((num_cities, num_cities))


for d in data:
    c1, c2 = d[0], d[2]

    for k, c in enumerate(cities):
        if c == c1: i = k
        if c == c2: j = k

    dists[i, j] = dists[j, i] = d[-1]

# this generates all permutations of possible routes
all_perms = itertools.permutations

def getRouteDist(route):
    return int(sum(dists[route[i], route[i+1]] for i in xrange(len(route)-1)))

print 'part a:', min(getRouteDist(route) for route in list(all_perms(cities_i)))
print 'part b:', max(getRouteDist(route) for route in list(all_perms(cities_i)))

