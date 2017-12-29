#!/usr/bin/env python

def part1(data):
    count, idx, N = 0, 0, len(data)
    while True:
        jump = data[idx]
        data[idx] += 1
        idx += jump
        count += 1
        if idx < 0 or idx >= N:
            break
    return count

def part2(data):
    count, idx, N = 0, 0, len(data)
    while True:
        jump = data[idx]
        if jump >= 3: data[idx] -= 1
        else: data[idx] += 1
        idx += jump
        count += 1
        if idx < 0 or idx >= N:
            break
    print data
    return count

data = [int(l.rstrip('\n')) for l in open('day05.in')]
assert(part1([0, 3, 0, 1, -3]) == 5)
print "answer (part1):", part1(data)

data = [int(l.rstrip('\n')) for l in open('day05.in')]
assert(part2([0, 3, 0, 1, -3]) == 10)
print "answer (part2):", part2(data)
