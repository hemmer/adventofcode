#!/usr/bin/env python

from hashlib import md5

key = 'iwrupvqb'
part_a = True

for i in xrange(20000000):
    string="%s%d" % (key, i)

    m = md5()
    m.update(string)
    hh = m.hexdigest()

    if part_a and hh[:5] == "00000":
        print "part a:", i, hh, string
        part_a = False

    if not part_a and hh[:6] == "000000":
        print "part b:", i, hh, string
        break
