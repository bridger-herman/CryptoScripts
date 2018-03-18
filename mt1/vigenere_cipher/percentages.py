#  https://en.wikipedia.org/wiki/Letter_frequency

percentages = [8.167,
1.492,
2.782,
4.253,
12.702,
2.228,
2.015,
6.094,
6.966,
0.153,
0.772,
4.025,
2.406,
6.749,
7.507,
1.929,
0.095,
5.987,
6.327,
9.056,
2.758,
0.978,
2.360,
0.150,
1.974,
0.074]


# Shift a list by one
def shift_list(l):
    return [l[-1]] + l[:-1]

perc = [p/100 for p in percentages]

percs_shifted = []
shifted = perc
for i in range(26):
    percs_shifted.append(shifted)
    shifted = shift_list(shifted)
