#!/usr/bin/env python

import re

def countChars(string):
    string = string[1:-1]
    string = string.replace('\\\\', '_')
    string = string.replace('\\"', '_')
    string = re.sub(r'\\x[0-9a-z][0-9a-z]', '_', string)
    return len(string)


def encodeLen(string):
    string = string.replace('\\\\', 'A')
    string = string.replace('\\\"', 'B')
    string = string.replace('\"', 'C')
    string = string.replace('\\x', 'D')

    # must make all replacements at once, so use
    # chars A-D to act as variables
    string = string.replace('A', '\\\\\\\\')
    string = string.replace('B', '\\\\\\\"')
    string = string.replace('C', '\\\"')
    string = string.replace('D', '\\\\x')

    string = '"' + string + '"'
    return len(string)

data = [line.rstrip('\n') for line in open('day08.in')]
print 'part a:', sum(len(d) - countChars(d) for d in data)
print 'part b:', sum(encodeLen(d) - len(d) for d in data)

