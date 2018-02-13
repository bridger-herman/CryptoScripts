# Vigenere Cipher decryption, Friedman Table
# Bridger Herman
# February 2018

import os
import sys
import math
from percentages import perc, percs_shifted

MAX_SHIFT = 50
LARGE_CUTOFF = 0.067

DB = 'debug' in sys.argv
dbprint = print if DB else lambda *args, **kwargs: None

# Shift a list by one
def shift_list(l):
    return [l[-1]] + l[:-1]

# Percent matches for two lists
def match_percent(l1, l2):
    assert len(l1) == len(l2)
    matches = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            matches += 1
    return matches/len(l1)

# Gets indices that are greater than a certain probability
def large_indices(l):
    return [i for i in range(len(l)) if l[i] > LARGE_CUTOFF]

# gcd of n numbers
def gcd_n(nums):
    if len(nums) < 2:
        raise ValueError
    elif len(nums) == 2:
        return math.gcd(nums[0], nums[1])
    else:
        return gcd_n([math.gcd(nums[i], nums[i+1]) for i in range(len(nums) - 1)])

# Probability for each letter in a list (using 0=a .. 25=z)
def letter_prob(l):
    return [l.count(n)/len(l) for n in range(26)]

# l1 and l2 (elementwise multiplication)
def dot(l1, l2):
    assert len(l1) == len(l2)
    return sum([l1[i]*l2[i] for i in range(len(l1))])

def decrypt(ciphertext):
    ciphernums = list(map(lambda l: ord(l) - 65, ciphertext.strip().upper()))
    friedman_table = [1] # 100% match for 0 shift
    shifted = shift_list(ciphernums)
    for shift in range(1, MAX_SHIFT + 1):
        friedman_table.append(match_percent(ciphernums, shifted))
        shifted = shift_list(shifted)

    dbprint('Friedman table:', [float(format(f, '.3f')) for f in friedman_table])

    # Cut off first element because shift 0
    indices = large_indices(friedman_table)[1:]
    dbprint('indices with high matches:', indices)

    # Key length is (probably) just the greatest common factor of the indices
    # with large percentage matches
    key_length = gcd_n(indices)
    dbprint('key length:', key_length)

    # Find the probabilities associated with each subsampled key (every
    # key_length items, modulo key_length)
    key_probabilities = [letter_prob(ciphernums[shift::key_length]) for shift
            in range(key_length)]

    # Actually construct the key, based on probability dot product with
    # Engilsh language letter frequency
    key_shifts = []
    for prob in key_probabilities:
        max_prob = 0
        max_index = 0
        for i in range(26):
            assert len(percs_shifted[i]) == len(prob)
            d = dot(prob, percs_shifted[i])
            if d > max_prob:
                max_prob = d
                max_index = i
        key_shifts.append(max_index)
    key = ''.join([chr(ki + 97) for ki in key_shifts])
    dbprint('key integers:', key_shifts)
    print('key:', key)

    # Decrypt the ciphertext
    plaintext_nums = []
    key_index = 0
    for n in ciphernums:
        if key_index >= len(key):
            key_index = 0
        plaintext_nums.append((n - key_shifts[key_index])%26)
        key_index += 1

    return ''.join(chr(n + 97) for n in plaintext_nums)

def main():
    if len(sys.argv) < 2:
        print('bad argument')
        print('vigenere.py ciphertext')
        return
    if os.path.isfile(sys.argv[1]):
        print(decrypt(open(sys.argv[1]).read()))
    else:
        print(decrypt(sys.argv[1]))

if __name__ == '__main__':
    main()
