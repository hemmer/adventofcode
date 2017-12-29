#!/usr/bin/env python

import numpy as np

class Coord():
    def __init__(self, x, y, val = 0):
        self.x = x
        self.y = y

    def step(self, dir):
        if dir == 0: self.y += 1
        elif dir == 1: self.x += 1
        elif dir == 2: self.y -= 1
        elif dir == 3: self.x -= 1

def print_state(pos, grid):

    for j in range(-4, 6)[::-1]:
        for i in range(-4, 6):
            if pos.x == i and pos.y == j:
                print "X",
                continue

            v = getgrid(i, j, grid)
            if   v == 2: print "#",
            elif v == 1: print "W",
            elif v == 3: print "F",
            else: print ".",
        print
    print

def setgrid(i, j, grid, val):
    N = len(grid)
    i_, j_ = i + N/2, j + N/2
    grid[i_, j_] = val

def getgrid(i, j, grid):
    N = len(grid)
    i_, j_ = i + N/2, j + N/2
    return grid[i_, j_]

def update_state(pos, dir, grid, part):

    current_state = getgrid(pos.x, pos.y, grid)
    i, j = pos.x, pos.y


    if part == 1:
        if current_state == 2:
            setgrid(i, j, grid, 0)
            return (dir + 1) % 4, 0
        elif current_state == 0:
            setgrid(i, j, grid, 2)
            return (dir - 1) % 4, 2
        else:
            print i, j, current_state

    elif part == 2:

        # if weakened...
        if current_state == 1:
            setgrid(i, j, grid, 2)
            return dir, 2

        # if infected...
        elif current_state == 2:
            setgrid(i, j, grid, 3)
            return (dir + 1) % 4, 3

        # if flagged
        elif current_state == 3:
            setgrid(i, j, grid, 0)
            # reverse
            return (dir + 2) % 4, 0

        # add a weakened node
        setgrid(i, j, grid, 1)
        return (dir - 1) % 4, 1

def load_grid(filename = "day22.in"):

    grid = np.zeros((401, 401))
    for j, line in enumerate(open(filename)):
        l = line.rstrip('\n')
        N = len(l)/2

        for i, c in enumerate(l):
            if c in "#":
                setgrid(i - N, N - j, grid, 2)

    return grid

def solution(part):
    if part == 1: iterations = 10000
    else: iterations = 10000000

    # dir N - 0, E - 1, S - 2, W - 3
    pos, dir = Coord(0, 0), 0

    grid = load_grid()

    c, num_infected, num_flagged = 0, 0, 0
    while c < iterations:

        dir, type = update_state(pos, dir, grid, part)

        if type == 2:
            num_infected += 1

        pos.step(dir)
        c += 1

    answer_str = "answer (part %d): %d" % (part, num_infected)
    print answer_str

solution(part = 1)
solution(part = 2)
