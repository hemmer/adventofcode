#!/usr/bin/env python

from collections import Counter

class Node(object):
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def sum_children(self):
        total = sum(c.sum_children() for c in self.children) + self.data
        return total

    def find_unbalanced(self):
        totals = Counter([c.sum_children() for c in self.children])

        # if there there is only one item in collection,
        # then we are balanced
        if len(totals.most_common(2)) < 2:
            return None

        # the odd one out occurs only once
        odd_one_out = totals.most_common(2)[1][0]
        # find discrepancy
        diff = totals.most_common(2)[0][0] - totals.most_common(2)[1][0]

        # loop through child nodes
        for c in self.children:
            # to find the odd one out
            if c.sum_children() == odd_one_out:

                ub = c.find_unbalanced()
                # if that node is unbalanced, then keep recursing
                if ub: return ub
                # otherwise work out what correction is needed
                else:  return c.data + diff

def solution(filename):
    data = []
    for l in open(filename):
        lp = l.rstrip('\n').translate(None, '(),->').replace('  ', ' ').split(' ')
        data.append(lp)
    names = [d[0] for d in data]

    # remove children from the list,
    # so head node is only thing left
    for d in data:
        if len(d) > 2:
            for c in d[2:]:
                names.remove(c)
    start_node_name = names[0]

    def getItem(name):
        for d in data:
            if d[0] == name:
                return d

    def createNode(item):
        n = Node(item[0], int(item[1]))
        for c in item[2:]:
            n.add_child(createNode(getItem(c)))
        return n

    start = getItem(start_node_name)
    head = createNode(start)
    correction = head.find_unbalanced()

    return start_node_name, correction


assert(solution("day07.in2") == ("tknk", 60))

p1, p2 = solution("day07.in")
print "answer (part1):", p1
print "answer (part2):", p2
