#!/usr/bin/env python

class CircBuff():
    def __init__(self, step = 3):
        self.data = [0]
        self.pos = 0
        self.step = step

    def add_val(self, val):
        N = len(self.data)
        self.pos = (self.pos + self.step) % N + 1
        self.data.insert(self.pos, val)

c = CircBuff()
for i in xrange(1, 2017 + 1):
    c.add_val(i)
assert(c.data[c.pos + 1] == 638)

c = CircBuff(343)
for i in xrange(1, 2017 + 1):
    c.add_val(i)
print "answer (part 1):", c.data[c.pos + 1]

pos, step, N, current = 0, 343, 50000000, 0
for i in xrange(1, N + 1):
    pos = (pos + step) % i + 1
    if pos == 1:
        current = i
print "answer (part 2):", current
