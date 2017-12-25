#!/usr/bin/env python

import sys


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Program():
    def __init__(self, filename, pid = 0):
        self.ins = []
        for line in open(filename):
            self.ins.append(line.rstrip('\n').split(' '))

        # contruct the register
        self.data = {}
        for i in self.ins:
            if not RepresentsInt(i[1]):
                self.data[i[1]] = 0

        self.data['a'] = 0

        self.jump = 1
        self.num_mul = 0
        self.pos = 0
        self.num_steps = 0

    def get(self, value):
        try:
            return int(value)
        except ValueError:
            return self.data[value]

    def proc_instr(self, ins, data):

        size = len(ins) - 1
        arg = self.get(ins[size])

        self.jump = 1

        if   ins[0] == "set": data[ins[1]] = arg
        elif ins[0] == "sub": data[ins[1]] -= arg
        elif ins[0] == "mul":
            data[ins[1]] *= arg
            self.num_mul += 1

        elif ins[0] == "jnz":

            check = self.get(ins[1])
            if check != 0:
                self.jump = arg
                return False
        else:
            print ins
            raise ValueError('Instruction not found')

        return False

    def step(self):
        waiting = self.proc_instr(self.ins[self.pos], self.data)
        self.pos += self.jump
        self.num_steps += 1
        if waiting or self.pos >= len(self.ins): return True
        else: return False

    def run(self):
        while self.pos < len(self.ins):
            if self.step():
                break
        return self.num_mul

p = Program("day23.in")
print "answer (part 1):", p.run()

