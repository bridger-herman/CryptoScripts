# Helper for computing polynomial roots in (Z/n)[x]
# Bridger Herman
# April 2018

from factor import factor
from order import order

# Compute all the orders of x^d - 1 in (Z/n)[x]
def pow_orders(d, n):
    fs = [1, d] + factor(d)
    for x in range(1, n):
        if order(x, n) in fs:
            print(x)

