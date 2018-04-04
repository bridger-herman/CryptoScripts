import sys
sys.path.append('../mt1')
from fastexp import modexp, exp
from math import log2
from factor import sieve

def fermat(n):
    for x in range(1, n):
        a = modexp(x, n - 1, n)
        if a != 1:
            print('Composite')
            return False
        else:
            print('Pseudoprime, base', x)
    return True

def fermat2(n):
    pseudos = []
    for x in range(1, n):
        a = modexp(x, n - 1, n)
        if a != 1:
            return (False, None)
        else:
            pseudos.append(x)
    return (True, pseudos)

# Is b a strong pseudoprime mod n
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

# Trial division of n
def trial_div(n):
    for k in range(3, int(n**0.5) + 1):
        print(k)
        if k % n == 0:
            return True
    return False

