# Subgroups
# Bridger Herman
# May 2018

import sys
import operator
sys.path.append('../mt1')

from euclid import modinv

# Find subgroups of integers modulo n
# Under addition
def z_subgroups(n, op):
    subgrps = []
    for start_el in range(n):
        x = start_el
        els = []
        while x != 0: # additive identity
            els.append(x)
            x = (op(x, start_el))%n
        s_els = sorted(els)
        if s_els not in subgrps:
            print(els)
            subgrps.append(s_els)
    for grp in subgrps:
        print('   ', sorted(grp))

# Find subgroups of integers modulo n
# Under addition
def z_x_subgroups(n, op):
    subgrps = []
    for start_el in range(n):
        try:
            modinv(start_el, n)
        except:
            continue
        x = start_el
        els = []
        while x != 0: # additive identity
            try:
                modinv(x, n)
                has_inv = True
            except:
                has_inv = False
            if has_inv:
                els.append(x)
            x = (op(x, start_el))%n
        s_els = sorted(els)
        if s_els not in subgrps:
            print(els)
            subgrps.append(s_els)
    for grp in subgrps:
        print('   ', sorted(grp))

