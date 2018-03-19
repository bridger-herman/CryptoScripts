# RSA Encryption
# Bridger Herman
# March 2018

import sys
sys.path.append('../mt1')

from euclid import egcd

# msg = message
# n = encryption modulus
# e = encryption exponent (assumes gcd(e, phi(n) = 1 and e < n))
def encrypt(msg, n, e):
    msg_clean = list(filter(lambda l: l.isalpha(), msg.strip().lower()))
    # a = 1, b = 2, etc.
    msg_nums = ''.join(map(lambda l: format(ord(l) - 96, '02'), msg_clean))
    m = int(msg_nums)
    return pow(m, e, n)

def alpha_to_num(msg):
    msg_clean = list(filter(lambda l: l.isalpha(), msg.strip().lower()))
    return int(''.join(map(lambda l: format(ord(l) - 96, '02'), msg_clean)))

def num_to_alpha(n):
    s = str(n)
    if len(s) % 2 != 0:
        s = "0" + s
    digits = []
    for i in range(0, len(s), 2):
        digits.append(s[i:i+2])
    return ''.join(map(lambda d: chr(int(d) + 96), digits))

def main():
    if len(sys.argv) != 4:
        print('bad argument')
        print('rsa.py plaintext modulus exponent')
        return
    print(encrypt(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))

if __name__ == '__main__':
    main()
