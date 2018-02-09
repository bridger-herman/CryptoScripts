# Vigenere Cipher decryption, Friedman Table
# Bridger Herman
# February 2018

import sys
import math
from percentages import perc, percs_shifted

MAX_SHIFT = 50
LARGE_CUTOFF = 0.067
#  MAX_SHIFT = 2

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
    ciphernums = list(map(lambda l: ord(l) - 65, ciphertext))
    friedman_table = [1] # 100% match for 0 shift
    shifted_lists = [ciphernums]
    shifted = shift_list(ciphernums)
    for shift in range(1, MAX_SHIFT + 1):
        shifted_lists.append(shifted)
        friedman_table.append(match_percent(ciphernums, shifted))
        shifted = shift_list(shifted)

    # Cut off first element because shift 0
    indices = large_indices(friedman_table)[1:]
    print(indices)

    # Key length is (probably) just the greatest common factor of the indices
    # with large percentage matches
    key_length = gcd_n(indices)

    probs0 = letter_prob(shifted_lists[0][::key_length])

    print(probs0)

    max_prob = 0
    max_index = 0
    for i in range(26):
        assert len(percs_shifted[i]) == len(probs0)
        d = dot(probs0, percs_shifted[i])
        if d > max_prob:
            max_prob = d
            max_index = i
    print(max_prob, max_index)

def main():
    if len(sys.argv) != 2:
        print('bad argument')
        print('vigenere.py ciphertext')
        return
    print(decrypt(open(sys.argv[1]).read().strip().upper()))
    #  print(decrypt(sys.argv[1].strip().upper()))

if __name__ == '__main__':
    main()
