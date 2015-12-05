#!/usr/bin/env python

import numpy as np
import scipy as sp

import hashlib


key = 'iwrupvqb'

for i in xrange(20000000):
    string="%s%07d" % (key, i)

    m = hashlib.md5()
    m.update(string)
    hh = m.hexdigest()

    if hh[:6] == "000000":
        print i, hh, string
        break

