#!/usr/bin/env python


class Generator():
    def __init__(self, start, factor, criterion = 0):
        self.val = start
        self.factor = factor
        self.mod = 2**16
        self.criterion = criterion

    def reset(self, start):
        self.val = start

    def next(self):
        v = self.val * self.factor
        self.val = v % 2147483647
        return self.val % self.mod

    def next_picky(self):
        invalid = True
        while invalid:
            self.next()
            if self.val % self.criterion == 0:
                invalid = False

        return self.val % self.mod

do_tests = True
if do_tests:
    startA, startB = 65, 8921
    gA = Generator(startA, 16807, 4)
    gB = Generator(startB, 48271, 8)

    N = 40000000
    assert(sum(1 for i in range(N) if gA.next() == gB.next()) == 588)

    gA.reset(startA)
    gB.reset(startB)
    N = 5000000
    assert(sum(1 for i in range(N) if gA.next_picky() == gB.next_picky())
            == 309)
    print "Tests passed!"



startA, startB = 277, 349
gA = Generator(startA, 16807, 4)
gB = Generator(startB, 48271, 8)

N = 40000000
part1 = sum(1 for i in range(N) if gA.next() == gB.next())
print "answer (part 1):", part1

gA.reset(startA)
gB.reset(startB)
N = 5000000
part2 = sum(1 for i in range(N) if gA.next_picky() == gB.next_picky())
print "answer (part 2):", part2
