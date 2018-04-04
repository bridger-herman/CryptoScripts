# RSA Encryption
# Bridger Herman
# March 2018

import sys
sys.path.append('../mt1')

from euclid import egcd
from alpha_helper import alpha_to_num

# msg = message
# n = encryption modulus
# e = encryption exponent (assumes gcd(e, phi(n) = 1 and e < n))
def encrypt(msg, n, e):
    m = alpha_to_num(msg)
    return pow(m, e, n)

def main():
    if len(sys.argv) != 4:
        print('bad argument')
        print('rsa.py plaintext modulus exponent')
        return
    print(encrypt(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))

if __name__ == '__main__':
    main()
