# Pollard's Rho and p-1 methods
# Bridger Herman
# May 2018

import sys
sys.path.append('../mt1')
from euclid import egcd
from math import log

def b_primes(b):
    primes = []
    with open('./10000_primes.csv') as fin:
        for line in fin:
            line = [int(p) for p in line.strip().split(',')]
            if max(line) <= b:
                primes.extend(line)
            else:
                up_to_max = [p for p in line if p <= b]
                primes.extend(up_to_max)
                break
    return primes


def pollard_rho(n):
    x = 2
    y = 2
    g = 1
    f = lambda x: (pow(x, 2, n) + 1)%n
    steps = 0
    while g == 1:
        #  print(g, x, y)
        x = f(x)
        y = f(f(y))
        g, _, _ = egcd(abs(x - y), n)
        steps += 1
    print(steps, 'steps')
    if g == n:
        return None
    else:
        return g

def pollard_p_1(n, bound=2):
    primes = b_primes(bound)
    t = len(primes)
    b = 2
    g, _, _ = egcd(b, n)
    if g >= 2:
        return g
    steps = 0
    for i in range(t):
        l = int(log(n)/log(primes[i]))
        r = pow(primes[i], l)
        b = pow(b, r, n)
        g, _, _ = egcd(b - 1, n)
        #  print(g, l, b)
        steps += 1
        if 1 < g and g < n:
            print(steps, 'steps')
            return g
        elif g == 1:
            continue
        elif g == n:
            print(steps, 'steps')
            return None
