#!/usr/bin/env python

def spin(s, X):
    return s[-X:] + s[0:-X]

def exchange(s, A, B):
    A_, B_ = s[A], s[B]
    s_ = list(s)
    s_[A] = B_
    s_[B] = A_
    return ''.join(s_)

def partner(s, A, B):
    s = s.replace(A, B.upper())
    s = s.replace(B, A)
    return s.lower()

s = "abcde"
assert(partner(exchange(spin(s, 1), 3, 4), 'e', 'b') == "baedc")

def one_pass(s, instrs):
    for i in instrs:
        f, args = i[0], i[1:]
        s = f(s, *args)
    return s

for line in open('day16.in'):
    line = line.rstrip('\n').split(',')

    # store instructions in array
    instrs = []
    for l in line:
        instr = l[0]
        remain = l[1:]
        if l[0] == 's':
            instrs.append([spin, int(remain)])
        if l[0] == 'x':
            l = map(int, remain.split('/'))
            instrs.append([exchange, l[0], l[1]])
        if l[0] == 'p':
            l = remain.split('/')
            instrs.append([partner, l[0], l[1]])

    N = int(1e9)
    s = 'abcdefghijklmnop'
    sols = []
    sols.append(s)
    for c in xrange(int(140**2)):
        s = one_pass(s, instrs)

        if c == 0:
            print "answer (part 1):", s

        sols.append(s)
        # if we have a repeat then quit
        if len(set(sols)) != len(sols):
            break
    cycle_length = c + 1

    # because cycle repeats, only need last cycle_length
    # iterations to get answer
    N = 1000000000
    for c in xrange(N % cycle_length):
        s = one_pass(s, instrs)

    print "answer (part 2):", s
