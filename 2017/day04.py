#!/usr/bin/env python

part1, part2 = 0, 0
for line in open('day04.in'):
    words = line.rstrip('\n').split(' ')
    if len(words) == len(set(words)):
        part1 += 1

    # sort each word, then apply the set test
    words = [''.join(w) for w in map(sorted, words)]
    if len(words) == len(set(words)):
        part2 += 1

print "answer (part1):", part1
print "answer (part2):", part2

