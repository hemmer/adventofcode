#!/usr/bin/env python

lines = [map(int, line.rstrip('\n').split('\t')) for line in open('day02.in')]

def part1(lines):
    return sum(max(line) - min(line) for line in lines)

def part2(lines):
    total = 0
    for line in lines:
        line = sorted(line)
        match = False

        for i, a in enumerate(line):
            if match: break
            for b in line[i+1:]:
                if b % a == 0:
                    total += b / a
                    match = True
                    break

    return total


assert(part1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18)
assert(part2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9)

print "answer (part 1):", part1(lines)
print "answer (part 2):", part2(lines)
