#!/usr/bin/env python

import numpy as np

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
        self.set_pos(start)
        vals = [self.next() for j in range(length)]
        for i, v in enumerate(vals[::-1]):
            self.l[(start + i) % self.N] = v

    def get_l(self):
        return self.l

def single_hash_pass(l, seq, pos = 0, skip_size = 0):

    N = len(l)
    a = CircList(l)
    for i in seq:
        a.permute_sublist(pos, i)
        inc = i + skip_size
        pos = (pos + inc) % N
        skip_size += 1

    vals = a.get_l()
    return vals[0] * vals[1], pos, skip_size, vals

def knot_hash(s):
    # convert every character to its ASCII value
    seq = [ord(c) for c in s]
    extra = [17, 31, 73, 47, 23]
    for e in extra:
        seq.append(e)

    # apply 64 passes of the hashing algorithm
    l, pos, skip_size = range(256), 0, 0
    for p in range(64):
        _, pos, skip_size, l = single_hash_pass(l, seq, pos, skip_size)

    # then condense down 16 blocks of 16 using the XOR operator
    xored = ""
    for i in range(16):
        bit = l[i*16:(i+1)*16]
        xored += format(reduce(lambda i, j: int(i) ^ int(j), bit), '02x')
    return xored

def c2b(c):
    return format(int(c, 16), '04b')

def recurse(i, j, index, grid):
    N = grid.shape[0]

    if grid[i, j] >= 0:
        return False
    else:
        grid[i, j] = index

    if i - 1 >= 0: recurse(i - 1, j, index, grid)
    if j - 1 >= 0: recurse(i, j - 1, index, grid)
    if i + 1 < N: recurse(i + 1, j, index, grid)
    if j + 1 < N: recurse(i, j + 1, index, grid)

    return True

sample = [3, 4, 1, 5]
assert(single_hash_pass(range(5), sample)[0] == 12)

total, N = 0, 128
grid = np.zeros((N, N))
for i in range(N):
    text = "ffayrhll-" + str(i)
    kh = knot_hash(text)

    print i, kh
    row = ''.join([c2b(c) for c in kh])
    squares = row.count("1")
    total += squares

    for j, c in enumerate(row):
        if c == "1":
            grid[i, j] = -1
print "answer (part 1):", total


index = 1
for i in range(N):
    for j in range(N):
        if recurse(i, j, index, grid):
            index += 1

print "answer (part 2):", int(np.max(grid))
