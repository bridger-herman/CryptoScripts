# Alphabetic helper functions
# Bridger Herman
# March 2018

# NOTE these assume 1 indexed
# a = 01, b = 02, etc.
# Change 96 to 97 if 00-index desired

# Convert string msg into an integer message
def alpha_to_num(msg):
    msg_clean = list(filter(lambda l: l.isalpha(), msg.strip().lower()))
    return int(''.join(map(lambda l: format(ord(l) - 96, '02'), msg_clean)))

# Convert an integer back into an ASCII string
def num_to_alpha(n):
    s = str(n)
    if len(s) % 2 != 0:
        s = "0" + s
    digits = []
    for i in range(0, len(s), 2):
        digits.append(s[i:i+2])
    return ''.join(map(lambda d: chr(int(d) + 96), digits))
