#!/usr/bin/env python


vs = dict()

def parseline(l):
    t, cond, val = l[-3:]
    val = int(val)

    if t not in vs: vs[t] = 0

    do_op = False
    if cond == ">" and vs[t] > val: do_op = True
    if cond == "<" and vs[t] < val: do_op = True
    if cond == "<=" and vs[t] <= val: do_op = True
    if cond == ">=" and vs[t] >= val: do_op = True
    if cond == "==" and vs[t] == val: do_op = True
    if cond == "!=" and vs[t] != val: do_op = True

    if do_op:
        var, op, val = l[:3]
        val = int(val)
        if var not in vs: vs[var] = 0

        if op == "inc": vs[var] += val
        if op == "dec": vs[var] -= val

def solution(filename):
    max_seen = 0
    for l in open(filename):
        l = l.rstrip('\n').split(' ')
        parseline(l)
        max_seen = max(max_seen, max(vs.values()))
    return max(vs.values()), max_seen

assert(solution("day08.in2") == (1, 10))

sol = solution("day08.in")
print "day 08 (part1):", sol[0]
print "day 08 (part2):", sol[1]


