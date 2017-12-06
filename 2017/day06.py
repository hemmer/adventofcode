#!/usr/bin/env python

import numpy as np
import collections

def sol(data):
    sols = collections.Counter()
    count, count_p1, count_p2, N = 0, 0, 0, len(data)

    while True:
        val, argmax = max(data), np.argmax(data)
        data[argmax] = 0
        for i in range(val):
            data[(1 + argmax + i) % N] += 1

        count += 1
        s = ' '.join(map(str, data))
        sols[s] += 1

        if not count_p1 and sols.most_common(1)[0][1] > 1:
            count_p1 = count

        if count_p1 and sols.most_common(1)[0][1] > 2:
            count_p2 = count - count_p1
            break

    return count_p1, count_p2


data = [map(int, l.rstrip('\n').split('\t')) for l in open('day06.in')][0]
assert(sol([0, 2, 7, 0]) == (5, 4))
print "answer:", sol(data)

