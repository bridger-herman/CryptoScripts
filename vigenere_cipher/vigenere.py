# Vigenere Cipher
# Bridger Herman
# February 2018

import sys

def encrypt(plaintext, key):
    plaintext_clean, key_clean = [list(filter(lambda l: l.isalpha(),
        string.strip().lower())) for string in [plaintext, key]]
    #  print(plaintext_clean, key_clean)
    plaintext_nums, key_nums = [list(map(lambda l: ord(l) - 97, string))
            for string in [plaintext_clean, key_clean]]
    #  print(plaintext_nums, key_nums)
    key_index = 0
    encrypted = ''
    for num in plaintext_nums:
        if key_index >= len(key):
            key_index = 0
        encrypted += chr((num + key_nums[key_index])%26 + 97)
        key_index += 1
    return encrypted



def main():
    if len(sys.argv) != 3:
        print('bad argument')
        print('vigenere.py plaintext key')
        return
    print(encrypt(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()
