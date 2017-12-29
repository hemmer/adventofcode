#!/usr/bin/env python

class Scanner():
    def __init__(self, x, height):
        self.height = height
        self.x = x

    def occupied(self, time, delay = 0):
        return (time + delay) % (2 * (self.height - 1)) == 0

def get_height(x, scanners):
    for s in scanners:
        if s.x == x: return s.height
    return None

def is_occupied(scanners, time, delay):
    for s in scanners:
        if s.x == time:
            return s.occupied(time, delay)
    return False

def read_input(filename):
    # read input from file
    scanners = []
    for line in open(filename):
        pos, height = map(int, line.rstrip('\n').split(': '))
        scanners.append(Scanner(pos, height))
    return scanners

def solution(scanners, delay = 0):

    max_x = max(s.x for s in scanners)

    caught = False
    packet_pos, severity = 0, 0

    for t in range(max_x + 1):
        if is_occupied(scanners, packet_pos, delay):
            severity += packet_pos * get_height(packet_pos, scanners)
            caught = True
            if delay and caught:
                return severity, caught
        packet_pos += 1

    return severity, caught

scanners = read_input("day13.in2")
assert(solution(scanners)[0] == 24)

for d in range(1, 15):
    severity, caught = solution(scanners, d)
    if not caught: break
assert(d == 10)

scanners = read_input("day13.in")
print solution(scanners)[0]

d, caught = 1, True
while caught:
    severity, caught = solution(scanners, d)
    d += 1

    if d % 1000 == 0:
        print d, severity, caught

print "answer (part 2):", d
