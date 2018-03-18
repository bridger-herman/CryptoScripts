# Affine Cipher
# Bridger Herman
# February 2018
import sys
sys.path.append('..')
from euclid import modinv
from debug import *


def encrypt(plaintext, a, k):
    plaintext_nums = list(map(lambda l: ord(l) - 97, filter(lambda l:
        l.isalpha(), plaintext.strip().lower())))
    dbprint('plaintext:', plaintext_nums)
    encrypted = [(num*a + k)%26 for num in plaintext_nums]
    dbprint('encrypted:', encrypted)

    return ''.join(map(lambda n: chr(n + 65), encrypted))

def decrypt(ciphertext, a=None, k=None):
    ciphertext_nums = list(map(lambda l: ord(l) - 65, filter(lambda l:
        l.isalpha(), ciphertext.strip().upper())))
    dbprint('ciphertext:', ciphertext_nums)
    if a is None and k is None:
        i = 0
        # Have inverses mod 26
        print(' a  k')
        for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            for k in range(26):
                i += 1
                decrypted = [(modinv(a, 26)*(num - k))%26 for num in
                        ciphertext_nums]
                print('{:02d} {:02d}'.format(a, k), ''.join(map(lambda n: chr(n
                    + 97), decrypted)))
                if i >= 3: # Stop every 3 elements for chunking
                    res = input('\nnext [enter]')
                    if res != '':
                        return
                    i = 0
    else:
        decrypted = [(modinv(a, 26)*(num - k))%26 for num in ciphertext_nums]
        dbprint('decrypted:', decrypted)
        return ''.join(map(lambda n: chr(n + 97), decrypted))

def main():
    if len(sys.argv) < 3:
        print('bad argument')
        print('affine.py <encrypt/decrypt> <plaintext/ciphertext> [a] [k]')
        return
    if sys.argv[1] == 'encrypt':
        if len(sys.argv) < 5:
            print('Need a and k')
            return
        print(encrypt(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))
    elif sys.argv[1] == 'decrypt':
        if len(sys.argv) < 5:
            print(decrypt(sys.argv[2]))
        else:
            print(decrypt(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))

if __name__ == '__main__':
    main()
