#!/usr/bin/env python

def part1(s):
    total, prev = 0, s[-1]

    for c in s:
        if c == prev:
            total += int(c)
        prev = c

    return total

def part2(s):
    length = len(s)
    offset = length / 2
    total = 0

    for i, c in enumerate(s):
        if c == s[(i + offset) % length]:
            total += int(c)

    return total


assert(part1("1122") == 3)
assert(part1("1111") == 4)
assert(part1("1234") == 0)
assert(part1("91212129") == 9)

assert(part2("1212") == 6)
assert(part2("1221") == 0)
assert(part2("123425") == 4)
assert(part2("123123") == 12)
assert(part2("12131415") == 4)

for line in open('day01.in'):
    l = line.rstrip('\n')
    print "answer (part 1):", part1(l)
    print "answer (part 1):", part2(l)





