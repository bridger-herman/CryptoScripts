# Recursive euclidean algorithm for GCD and modular inverse
import sys
sys.path.append('..')
from debug import *

# TODO make this https://stackoverflow.com/a/9758173
def egcd(a, b):
    dbprint('euclidean', a, b)
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd2(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        t = b
        q = a//b
        b = a%b
        print('{} = {}*{} + {}'.format(a, q, t, b))
        a = t
    return a
