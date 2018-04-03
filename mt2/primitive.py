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

# is x primitive modulo p
def is_primitive(x, p):
    for q in factor(p - 1):
        if len(factor(q)) == 0:
            v = (x**((p - 1)/q) % p)
            #  print('testing {}**(({} - 1)/{}) % {} = {}'.format(x, p, q, p, v))
            if v == 1:
                return False
    return True

# Primitive elements, modulo m
def primitives_of(m):
    assert len(factor(m)) == 0
    for i in range(1, m):
        if is_primitive(i, m):
            print(i)
