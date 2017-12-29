#!/usr/bin/env python

class Node(object):
    def __init__(self, nid):
        self.nid = nid
        self.children = []
        self.visited = False

    def add_child(self, obj):
        self.children.append(obj)

def getNode(nodes, nid):
    for n in nodes:
        if n.nid == nid:
            return n
    return None

def visitChildren(children):
    count = 0
    for c in children:
        if not c.visited:
            c.visited = True
            count += 1
            count += visitChildren(c.children)
    return count

def solution(filename):

    # read input from file
    lines = []
    for line in open(filename):
        l = line.rstrip('\n')
        lp = map(int, l.translate(None, '<,->').replace('  ', ' ').split(' '))
        lines.append(lp)

    # create list of nodes
    nodes = []
    for l in lines:
        nodes.append(Node(l[0]))

    # populate child nodes
    for l in lines:
        for c in l[1:]:
            getNode(nodes, l[0]).add_child(getNode(nodes, c))

    # count (a) number in group 0 and (b) number of groups
    num_in_group_zero, groups = 0, 0
    for i, n in enumerate(nodes):
        num_in_group = visitChildren(n.children)
        if i == 0:
            num_in_group_zero = num_in_group
        if num_in_group > 0:
            groups += 1

    return num_in_group_zero, groups

assert(solution("day12.in2") == (6, 2))

num_in_group_zero, groups = solution("day12.in")
print "answer (part1):", num_in_group_zero
print "answer (part2):", groups
