#!/usr/bin/env python

# part 6b
array = np.zeros((1000,1000), dtype=bool)

def processCmd(cmd):

    cmd = cmd.split(' ')
    print cmd

    x1, y1 = map(int, cmd[-3].split(','))
    x2, y2 = map(int, cmd[-1].split(','))
    print x1, x2, y1, y2

    for i in xrange(x1,x2+1):
        for j in xrange(y1,y2+1):
            if cmd[0] == 'turn':
                if cmd[1] == 'on': array[i, j] = True
                if cmd[1] == 'off': array[i, j] = False
            if cmd[0] == 'toggle':
                array[i, j] = not array[i, j]


for line in open('day06.in'):
    line = line.rstrip('\n')
    processCmd(line)

print np.sum(array), 1000*1000





# part 6b
array = np.zeros((1000,1000))

def processCmd2(cmd):

    cmd = cmd.split(' ')
    print cmd

    x1, y1 = map(int, cmd[-3].split(','))
    x2, y2 = map(int, cmd[-1].split(','))
    print x1, x2, y1, y2

    for i in xrange(x1,x2+1):
        for j in xrange(y1,y2+1):
            if cmd[0] == 'turn':
                if cmd[1] == 'on':
                    array[i, j] = array[i, j] + 1
                if cmd[1] == 'off':
                    array[i, j] = array[i, j] - 1
                    if array[i, j] < 0:
                        array[i, j] = 0
            if cmd[0] == 'toggle':
                array[i, j] = array[i, j] + 2


for line in open('day06.in'):
    line = line.rstrip('\n')
    processCmd2(line)

print np.sum(array), 1000*1000
