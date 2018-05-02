# Jacobi Symbol
# Bridger Herman
# May 2018

import sys
sys.path.append('../mt2')
from factor import sieve

# NOTE: don't call this on large numbers
def jacobi_prime(a, p):
    assert sieve(p)
    return pow(a, round((p-1)/2), p)

