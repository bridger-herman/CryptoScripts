# Various factoring functions
# Bridger Herman
# March 2018

# Return factors of n (other than 1 and n)
def factor(n):
    non_divisors = []
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
        #  for d in non_divisors:
            #  if i % d == 0:
    return factors

# Copied from here https://stackoverflow.com/a/17377939
# Could've done this myself but ran out of time
# Sieve of Eratosthenes
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
