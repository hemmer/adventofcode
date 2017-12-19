#!/usr/bin/env python

import numpy as np

def solution(filename):
    # load in data
    diag = np.array([list(line.rstrip('\n')) for line in open(filename)])

    # find starting position
    start_x, start_y = np.where(diag[0, :] == "|")[0][0], 0
    pos = np.array([start_x, start_y])

    # N - 0, E - 1, S - 2, W - 3 (N/S opposite for easy array math)
    d, dirs = 2, ((0, -1), (1, 0), (0, +1), (-1, 0))

    letters, c = [], 0
    while True:
        val = diag[pos[1], pos[0]]

        # if we dont have a charater associated with the
        # piping, we are either collection letters or finished
        if val not in "|-+":
            if val == " ":
                break
            letters.append(val)
            if d == 0 or d == 2:
                diag[pos[1], pos[0]] = "|"
            else:
                diag[pos[1], pos[0]] = "-"

        # we only care if we are at a junction
        else:
            if val == "+":
                for i, n in enumerate(dirs):
                    # don't come back the way we came
                    if i == (d + 2) % 4:
                        continue

                    # try each position - if there is a
                    # non-empty square then go there!
                    pos_new = pos + dirs[i]
                    if diag[pos_new[1], pos_new[0]] != " ":
                        d = i
                        break

        # step on!
        pos += dirs[d]
        c += 1
    return "".join(letters), c

assert(solution("day19.in2") == ('ABCDEF', 38))

part1, part2 = solution("day19.in")
print "answer (part 1):", part1
print "answer (part 2):", part2
