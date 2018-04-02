import sys
sys.path.append('../mt1')
from fastexp import modexp, exp
from math import log2

def fermat(n):
    for x in range(1, n):
        a = modexp(x, n - 1, n)
        if a != 1:
            print('Composite')
            return False
        else:
            print('Pseudoprime, base', x)

def strong_pseudo(b, n):
    for m in range(1, n):
        r = int(log2((n - 1)//m))
        e = modexp(b, m, n)
        for s in range(1, r):
            e2 = modexp(b, exp(2, s)*m, n)
            if e == 1 or e2 == -1:
                print('Strong pseudoprime m={}, r={}, s={}'.format(m, r, s),
                        end=" ")
                if e == 1:
                    print('(condition 1)')
                if e == -1:
                    print('(condition 2)')
