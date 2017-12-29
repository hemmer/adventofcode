#!/usr/bin/env python

def parseline(line):
    groups = []
    num_groups = 0
    skip_next = False
    in_garbage = False
    score = 0
    garbage_count = 0
    for c in line:

        if skip_next:
            skip_next = False
            continue

        if c == "!":
            skip_next = True
            continue
        elif c == "<":
            if not in_garbage:
                in_garbage = True
                continue
        elif c == ">":
            in_garbage = False

        if in_garbage:
            garbage_count += 1
            continue

        if c == "{":
            score += len(groups) + 1
            groups.append('{')
        elif c == "}":
            groups.pop()
            num_groups += 1

    return score, garbage_count

assert(parseline("{{{},{},{{}}}}")[0] == 16)
assert(parseline("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9)
assert(parseline("<random characters>")[1] == 17)
assert(parseline('<{o"i!a,<{i<a>')[1] == 10)

for l in open("day09.in"):
    l = l.rstrip('\n')
    sol = parseline(l)
    print "answer (part 1):", sol[0]
    print "answer (part 2):", sol[1]
