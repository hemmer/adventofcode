#!/usr/bin/env python

import numpy as np
import scipy as sp

class CircList(object):
    def __init__(self, l):
        self.l = l
        self.N = len(self.l)
        self.pos = 0

    def next(self):
        val = self.l[self.pos]
        self.pos = (self.pos + 1) % self.N
        return val

    def set_pos(self, pos):
        self.pos = pos

    def permute_sublist(self, start, length):
        #  if length == 1: return
        self.set_pos(start)
        vals = [self.next() for j in range(length)]
        for i, v in enumerate(vals[::-1]):
            self.l[(start + i) % self.N] = v

    def get_l(self):
        return self.l


def part1(l, seq, pos = 0, skip_size = 0, extra = []):

    for e in extra:
        seq.append(e)

    N = len(l)
    a = CircList(l)
    for i in seq:
        a.permute_sublist(pos, i)
        inc = i + skip_size
        pos = (pos + inc) % N
        skip_size += 1

    vals = a.get_l()
    return vals[0] * vals[1], pos, skip_size, vals

sample = [3, 4, 1, 5]
assert(part1(range(5), sample)[0] == 12)


for line in open("day10.in"):
    seq = line.rstrip('\n').split(',')
    seq = map(int, seq)
    print part1(range(256), seq)[0]

    seq = [ord(c) for c in line.rstrip('\n')]
    extra = [17, 31, 73, 47, 23]

    l, pos, skip_size = range(256), 0, 0
    for p in range(64):
        _, pos, skip_size, l = part1(l, seq, pos, skip_size, extra)

    print l
    xored = ""
    for i in range(16):
        bit = l[i*16:(i+1)*16]
        xored += format(reduce(lambda i, j: int(i) ^ int(j), bit), '02x')
    print xored

