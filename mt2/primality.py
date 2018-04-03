import sys
sys.path.append('../mt1')
from fastexp import modexp, exp
from math import log2

# Copied from here https://stackoverflow.com/a/17377939
# Could've done this myself but ran out of time
def sieve(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

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

