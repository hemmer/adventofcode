#!/usr/bin/env python

data = [line.rstrip('\n') for line in open('day07.in')]
dit = {ins.split(' ')[-1]: ins.split(' ') for ins in data}

allf = 0xFFFF

def recurse(ins):
    if len(ins) == 5:
        try: arg1 = int(ins[0])
        except: arg1 = recurse(dit[ins[0]])
        try: arg2 = int(ins[2])
        except: arg2 = recurse(dit[ins[2]])

        if ins[1] == 'OR':
            dit[ins[-1]] = [str(arg1 | arg2), '->', ins[-1]]
            return arg1 | arg2
        if ins[1] == 'AND':
            dit[ins[-1]] = [str(arg1 & arg2), '->', ins[-1]]
            return arg1 & arg2
        if ins[1] == 'LSHIFT':
            dit[ins[-1]] = [str(arg1 << arg2), '->', ins[-1]]
            return arg1 << arg2
        if ins[1] == 'RSHIFT':
            dit[ins[-1]] = [str(arg1 >> arg2), '->', ins[-1]]
            return arg1 >> arg2

    elif ins[0] == 'NOT':
        try: arg1 = int(ins[1])
        except: arg1 = recurse(dit[ins[1]])
        return ~ arg1 & allf
    elif len(ins) == 3:
        try:    return int(ins[0])
        except: return recurse(dit[ins[0]])


answer = recurse(dit['a'])
print "part a:", answer

data = [line.rstrip('\n') for line in open('day07.in')]
dit = {ins.split(' ')[-1]: ins.split(' ') for ins in data}
dit['b'] = [str(answer), '->', 'b']
print "part b:", recurse(dit['a'])
