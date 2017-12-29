#!/usr/bin/env python

dirs = [+1, 0, -1, 0]

def part1(N):

    nums = range(1, N+1)
    w, h = 1, 1
    x, y = 0, 0
    xi, yi = 0, 3

    for n in nums[1:]:
        x += dirs[xi]
        y += dirs[yi]
        if x == w:
            xi = (xi + 1) % 4
            yi = (yi + 1) % 4
            if w > 0: w = -w
            else:     w = -w + 1
        if y == h:
            xi = (xi + 1) % 4
            yi = (yi + 1) % 4
            if h > 0: h = -h
            else:     h = -h + 1

    return abs(x) + abs(y)

assert(part1(1) == 0)
assert(part1(12) == 3)
assert(part1(23) == 2)
assert(part1(1024) == 31)

print "answer (part1):", part1(325489)

def neighbours(x, y):
    n = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            n.append([i, j])
    return n

def getValue(x, y, nums):
    nbs = neighbours(x, y)
    val = 0
    for nb in nbs:
        for n in nums[::-1]:
            if n[0] == nb[0] and n[1] == nb[1]:
                val += n[2]
    return val

def part2(val):

    nums = [[0, 0, 1]]
    w, h = 1, 1
    x, y = 0, 0
    xi, yi = 0, 3

    while nums[-1][2] < val:
        x += dirs[xi]
        y += dirs[yi]

        v = getValue(x, y, nums)

        if x == w:
            xi = (xi + 1) % 4
            yi = (yi + 1) % 4
            if w > 0: w = -w
            else:     w = -w + 1
        if y == h:
            xi = (xi + 1) % 4
            yi = (yi + 1) % 4
            if h > 0: h = -h
            else:     h = -h + 1

        nums.append([x, y, v])

    return nums[-1][2]

print "answer (part2):", part2(325489)
