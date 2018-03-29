import sys
sys.path.append('../mt1')
from fastexp import modexp

def fermat(n):
    for x in range(1, n):
        a = modexp(x, n - 1, n)
        if a != 1:
            print('Composite')
            return False
        else:
            print('Pseudoprime, base', x)
