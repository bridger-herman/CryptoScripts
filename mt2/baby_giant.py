import sys
sys.path.append('../mt1')

from euclid import modinv
from fastexp import modexp
from primitive import is_primitive

#  https://en.wikipedia.org/wiki/Baby-step_giant-step
def disc_log(a, b, p):
    m = int(p**0.5) + 1 # Ceiling
    pairs = []
    for j in range(m):
        pairs.append((j, modexp(a, j, p)))
    am = modexp(modinv(a, p), m, p) # a^(-m) mod p -> (a^(-1))^m mod p
    ajs = (list(zip(*pairs))[1])
    y = b
    for i in range(m):
        if y in ajs:
            return i*m + pairs[ajs.index(y)][0] # i*m + j
        else:
            y = (y*am) % p
