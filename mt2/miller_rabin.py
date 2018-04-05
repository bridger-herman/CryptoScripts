# Miller-Rabin Test
# Bridger Herman
# April 2018

import sys
sys.path.append('../mt1')

from math import log2, gcd
from fastexp import exp
from random import randint

# False = composite
# True = probably prime
def miller_rabin(n, x=None):
    # Get o (odd)
    j = 1
    k = 0
    found = False
    while j < n - 1 and not found:
        j <<= 1
        for o in range(n - 1):
            if o*j == n - 1 and o % 2 != 0:
                found = True
                break
        k += 1
    if not found:
        raise ValueError('Odd number not found')

    # Choose an x
    if x is None:
        x = randint(1, n - 1)
        while gcd(x, n) != 1:
            x = randint(1, n - 1)
        print('base', x)

    # Compute M-R sequence (last term first)
    mr_sequence = (exp(x, (n-1)/(1<<i)) for i in range(k))
    print('M-R sequence:')
    for i, term in enumerate(mr_sequence):
        print('  x^((n-1)/(2^i)) = {}^(({}-1)/(2^{})) = {}'.format(x, n, i,
            term%n))
    for term in mr_sequence:
        m = term % n
        if m != 1 and m != -1:
            return False
        elif m != -1:
            return True
    return True
