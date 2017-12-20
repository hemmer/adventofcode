#!/usr/bin/env python

import numpy as np

class Particle():
    def __init__(self, p, v, a):
        self.p = np.array(p)
        self.v = np.array(v)
        self.a = np.array(a)

def solution(filename, part2 = False):

    # load in data
    ps = []
    for line in open(filename):
        l = line.rstrip('\n').split(', ')
        p, v, a = [map(int, block[3:-1].split(',')) for block in l]
        ps.append(Particle(p, v, a))

    tmax = 500
    if part2: tmax = 50

    steps = 0
    while steps < tmax:
        min_dist = int(1e9)
        min_p = -1
        for i, p in enumerate(ps):
            p.v += p.a
            p.p += p.v

            dist = np.sum(np.abs(p.p))
            if dist < min_dist:
                min_dist = dist
                min_p = i

        if part2:
            collisions, del_idxs, N = True, set(), len(ps)
            for i in xrange(N):
                if i in del_idxs: continue

                for j in xrange(i+1, N):
                    if j in del_idxs: continue

                    if np.array_equal(ps[i].p, ps[j].p):
                        del_idxs.add(i)
                        del_idxs.add(j)

            del_idxs = list(del_idxs)
            if del_idxs:
                # delete elements (in reverse order to avoid
                # messing up index positions)
                for idx in sorted(del_idxs, reverse=True):
                    del ps[idx]

        steps += 1

    return min_p, len(ps)

print "answer (part 1):", solution("day20.in")[0]
print "answer (part 2):", solution("day20.in", True)[1]
