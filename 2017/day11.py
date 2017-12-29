#!/usr/bin/env python

def walk(x, y, z, ins):
    ins = ins.split(',')
    max_dist = 0
    for i in ins:
        if i == "n":
            y += 1
            z -= 1
        elif i == "s":
            y -= 1
            z += 1

        elif i == "nw":
            x -= 1
            y += 1
        elif i == "se":
            x += 1
            y -= 1

        elif i == "ne":
            x += 1
            z -= 1
        elif i == "sw":
            z += 1
            x -= 1

        else:
            print "error:", i
            return
        dist = (abs(x) + abs(y) + abs(z)) / 2
        max_dist = max(dist, max_dist)

    return dist, max_dist

x, y, z = 0, 0, 0

assert(walk(x, y, z, "se,sw,se,sw,sw")[0] == 3)
assert(walk(x, y, z, "ne,ne,sw,sw")[0] == 0)
assert(walk(x, y, z, "ne,ne,s,s")[0] == 2)
assert(walk(x, y, z, "se,sw,se,sw,sw")[0] == 3)
assert(walk(x, y, z, "ne,ne,ne")[0] == 3)
assert(walk(x, y, z, "se,se,n,n")[0] == 2)
assert(walk(x, y, z, "ne,se,sw,nw")[0] == 0)

x, y = 0, 0
for line in open("day11.in"):
    l = line.rstrip('\n')
    print walk(x, y, z, l)
