# Fast exponentiation algorithm (from Garret notes)
# Bridger Herman
# March 2018

def exp(x, e):
    y = 1
    while e != 0:
        print('{: 8} & {: 8} & {: 8} \\\\'.format(x, e, y))
        if e % 2 != 0:
            y = x*y
            e = e - 1
        else:
            x = x*x
            e = e//2
    return y

def modexp(x, e, m):
    y = 1
    while e != 0:
        print('{: 8} & {: 8} & {: 8} \\\\'.format(x, e, y))
        if e % 2 != 0:
            y = (x*y) % m
            e = e - 1
        else:
            x = (x*x) % m
            e = e//2
    print('{: 8} & {: 8} & {: 8} \\\\'.format(x, e, y))
    return y

