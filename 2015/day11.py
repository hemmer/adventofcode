#!/usr/bin/env python

def isValid(string):
    ascii =  map(ord, (list(string)))

    # first requirement
    firstTest = False
    for i in xrange(len(string)-3):
        if ascii[i] == ascii[i+1]-1 == ascii[i+2]-2:
            firstTest = True
            break

    # second requirement
    if "i" in string or "o" in string or "l" in string:
        secondTest = False
    else:
        secondTest = True

    # third requirement
    thirdTest = False
    for i in xrange(len(string)-1):
        if ascii[i] == ascii[i+1]:
            for j in xrange(i+2, len(string)-1):
                if ascii[j] == ascii[j+1]:
                    thirdTest = True
                    break

    return firstTest and secondTest and thirdTest

def incPassword(string):

    ascii =  map(ord, list(string))
    for i in xrange(len(ascii)):
        ascii[i] -= 97

    for i in xrange(len(ascii)):
        newVal = ascii[-(i+1)] + 1
        if newVal % 26 == 0:
            ascii[-(i+1)] = 0
            continue
        else:
            ascii[-(i+1)] = newVal
            break

    newPassword = ''.join(chr(int(a) + 97) for a in ascii)
    return newPassword



string = "hepxcrrq"

while not isValid(string):
    string = incPassword(string)
print string, isValid(string)

string = incPassword(string)

while not isValid(string):
    string = incPassword(string)
print string, isValid(string)
