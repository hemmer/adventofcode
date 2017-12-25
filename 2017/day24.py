#!/usr/bin/env python

class Node():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.used = False

def build_tree(connect, cpts, part):

    s, max_sum, max_length = 0, 0, 0
    for c in cpts:
        if c.used: continue

        c.used = True
        sub_sum, sub_length = 0, 0

        if c.p1 == connect:
            sub_sum, sub_length = build_tree(c.p2, cpts, part)
            sub_sum += c.p1 + c.p2
            sub_length += 1
        elif c.p2 == connect:
            sub_sum, sub_length = build_tree(c.p1, cpts, part)
            sub_sum += c.p1 + c.p2
            sub_length += 1
        c.used = False

        if sub_length >= max_length or part == 1:
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_length = sub_length

    return max_sum, max_length

def solution(part, filename = "day24.in"):
    temp = []
    lines = [map(int, line.rstrip('\n').split('/')) \
            for line in open(filename)]

    cpts = [Node(l[0], l[1]) for l in lines]

    return build_tree(0, cpts, part)[0]

assert(solution(part = 1, filename = "day24.in2") == 31)
assert(solution(part = 2, filename = "day24.in2") == 19)

print "answer (part 1):", solution(part = 1)
print "answer (part 2):", solution(part = 2)



