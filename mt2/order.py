# Order of n, modulo m
# TODO make more efficient
def order(n, m):
    e = 1
    found = False
    while not found:
        if (n**e) % m == 1:
            found = True
            return e
        e += 1
