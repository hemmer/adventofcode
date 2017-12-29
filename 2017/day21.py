#!/usr/bin/env python2.7

import numpy as np
from string import maketrans   # Required to call maketrans function.

class Rule():
    def __init__(self, input_str, output_str):
        self.input = self.s2r(input_str)
        self.output = self.s2r(output_str)

    def s2r(self, text):
        trantab = maketrans(".#", "01")
        return np.array([map(int, x) for x in map(list,
            text.translate(trantab).split('/'))], dtype=bool)

    def match_found(self, v):
        if len(self.input) != len(v):
            return False
        if np.sum(self.input) != np.sum(v):
            return False

        for r in range(4):
            v_rot = np.rot90(v, r)

            if np.array_equal(self.input, v_rot) or \
               np.array_equal(self.input, np.flipud(v_rot)) or \
               np.array_equal(self.input, np.fliplr(v_rot)):
                    return True

        return False

def divide(grid, rules):
    N = len(grid)
    if N % 2 == 0:
        new = []
        for i in xrange(N/2):
            col = []
            for j in xrange(N/2):
                col.append(apply_rule(grid[2*i:2*(i+1), 2*j:2*(j+1)], rules))
            new.append(col)
        return np.block(new)
    elif N % 3 == 0:
        new = []
        for i in xrange(N/3):
            col = []
            for j in xrange(N/3):
                col.append(apply_rule(grid[3*i:3*(i+1), 3*j:3*(j+1)], rules))
            new.append(col)
        return np.block(new)
    else:
        print "Errro"

    return None

def apply_rule(sub_grid, rules):

    for rule in rules:
        if rule.match_found(sub_grid):
            return np.array(rule.output)

    print sub_grid
    return None

grid = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

filename = "day21.in"
rules = []
for line in open(filename):
    r = line.rstrip('\n').split(" => ")
    rules.append(Rule(r[0], r[1]))

for i in range(18):
    grid = divide(grid, rules)
    if i == 4:
        print "answer (part 1):", np.sum(grid)
print "answer (part 2):", np.sum(grid)
