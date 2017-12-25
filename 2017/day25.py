#!/usr/bin/env python

import numpy as np

class State():
    def __init__(self, key, c0v, c0d, c0n, c1v, c1d, c1n):
        self.key = key
        self.c0v = c0v
        self.c0d = c0d
        self.c0n = c0n

        self.c1v = c1v
        self.c1d = c1d
        self.c1n = c1n


def solution(test = False):

    states = []
    if not test:
        states.append(State(0,  1, +1, 1,  0, -1, 4))
        states.append(State(1,  1, -1, 2,  0, +1, 0))
        states.append(State(2,  1, -1, 3,  0, +1, 2))
        states.append(State(3,  1, -1, 4,  0, -1, 5))
        states.append(State(4,  1, -1, 0,  1, -1, 2))
        states.append(State(5,  1, -1, 4,  1, +1, 0))

        num_check = 12208951
    else:
        states.append(State(0,  1, +1, 1,  0, -1, 1))
        states.append(State(1,  1, -1, 0,  1, +1, 0))

        num_check = 6

    current_state = 0
    N, pos = 10001, 0
    grid = np.zeros(N, dtype=int)
    for i in xrange(num_check):
        s = states[current_state]
        if grid[pos+N/2]:
            d, current_state = s.c1d, s.c1n
            grid[pos+N/2] = s.c1v
            pos += d
        else:
            d, current_state = s.c0d, s.c0n
            grid[pos+N/2] = s.c0v
            pos += d

    return np.sum(grid)



assert(solution(test = True) == 3)

print "answer (part 1):", solution()

