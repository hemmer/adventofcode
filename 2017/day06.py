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
        sols[tuple(data)] += 1
        max_num_occur = sols.most_common(1)[0][1]

        if not count_p1 and max_num_occur > 1:
            count_p1 = count

        if count_p1 and max_num_occur > 2:
            count_p2 = count - count_p1
            break

    return count_p1, count_p2


data = [map(int, l.rstrip('\n').split('\t')) for l in open('day06.in')][0]
assert(sol([0, 2, 7, 0]) == (5, 4))
print "answer:", sol(data)

