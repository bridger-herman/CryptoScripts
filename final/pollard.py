# Pollard's Rho and p-1 methods
# Bridger Herman
# May 2018

import sys
sys.path.append('../mt1')
from euclid import egcd

def pollard_rho(n):
    x = 2
    y = 2
    g = 1
    f = lambda x: (pow(x, 2, n) + 1)%n
    while g == 1:
        print(g, x, y)
        x = f(x)
        y = f(f(y))
        g, _, _ = egcd(abs(x - y), n)
    if g == n:
        return None
    else:
        return g
