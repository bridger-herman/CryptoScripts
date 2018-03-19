# Primitive elements/roots/generators
# Bridger Herman
# March 2018

def factor(n):
    non_divisors = []
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
        #  for d in non_divisors:
            #  if i % d == 0:
    return factors

def is_primitive(x, p):
    for q in factor(p - 1):
        if len(factor(q)) == 0 and (x*((p - 1)/q) % p) == 1:
            return False
    return True

