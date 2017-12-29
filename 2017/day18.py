#!/usr/bin/env python

last_played = 0

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
            self.data[i[1]] = 0

        self.pid = pid
        self.data['p'] = pid

        self.vals = []
        self.other = None
        self.jump = 1
        self.last_played = 0
        self.num_sent = 0
        self.pos = 0

    def set_other(self, other):
        self.other = other

    def get(self, value):
        try:
            return int(value)
        except ValueError:
            return self.data[value]

    def proc_instr(self, ins, data):
        # returns True if waiting for instruction,
        # otherwise false

        size = len(ins) - 1
        arg = self.get(ins[size])

        self.jump = 1

        if   ins[0] == "set": data[ins[1]] = arg
        elif ins[0] == "add": data[ins[1]] += arg
        elif ins[0] == "mul": data[ins[1]] *= arg
        elif ins[0] == "mod": data[ins[1]] %= arg
        elif ins[0] == "snd":

            if self.other:
                self.other.vals.append(arg)
                self.num_sent += 1
            else:
                self.last_played = data[ins[1]]

        elif ins[0] == "rcv":

            if self.vals:
                data[ins[1]] = self.vals.pop(0)
            else:
                self.jump = 0
                return True

        elif ins[0] == "jgz":

            check = self.get(ins[1])
            if check > 0:
                self.jump = arg
                return False
        else:
            print ins
            raise ValueError('Instruction not found')

        return False

    def step(self):
        waiting = self.proc_instr(self.ins[self.pos], self.data)
        self.pos += self.jump

        if waiting or self.pos >= len(self.ins): return True
        else: return False

    def run(self):
        while self.pos < len(self.ins):
            if self.step():
                break
        return self.last_played

p = Program("day18.in2")
assert(p.run() == 4)

p = Program("day18.in")
print "answer (part 1):", p.run()

filename = "day18.in"
p0 = Program(filename, 0)
p1 = Program(filename, 1)
p0.set_other(p1)
p1.set_other(p0)

dead = False
while not dead:
    p0waiting = p0.step()
    p1waiting = p1.step()

    if p0waiting and p1waiting:
        dead = True

print "answer (part 2):", p1.num_sent
