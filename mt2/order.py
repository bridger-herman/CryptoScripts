# Order of n, modulo m
# Bridger Herman
# April 2018

from fastexp import modexp

def order(n, m):
    e = 1
    found = False
    while not found:
        if modexp(n, e, m) == 1:
            found = True
            return e
        e += 1
