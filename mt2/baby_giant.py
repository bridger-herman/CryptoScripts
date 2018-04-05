import sys
sys.path.append('../mt1')

from euclid import modinv
from fastexp import modexp
from primitive import is_primitive

#  https://en.wikipedia.org/wiki/Baby-step_giant-step
# In the integers mod `p`, finding log_a(b)
def disc_log(a, b, p):
    m = int(p**0.5) + 1 # Ceiling
    print('m =', m)
    pairs = []
    for j in range(m):
        g = modexp(a, j, p)
        print('giant step a^j: {}^{} = {}'.format(a, j, g))
        pairs.append((j, g))
    am = modexp(modinv(a, p), m, p) # a^(-m) mod p -> (a^(-1))^m mod p
    print('a^{-m} =', am)
    ajs = (list(zip(*pairs))[1])
    y = b
    for i in range(m):
        s = (y*am) % p
        print('baby step y*am: {}*{} = {}'.format(y, am, s))
        if y in ajs:
            return i*m + pairs[ajs.index(y)][0] # i*m + j
        else:
            y = s
