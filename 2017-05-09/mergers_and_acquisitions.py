LEFTS = [
    #'FE',
    #'SE',
    #'NUE',
    #'HAR'
    #'GE'
    #'DO'
    'MA'
]

RIGHTS = '''A
BBY
COH
DG
DOW
ED
EL
ES
ESS
GE
IFF
K
KLAC
M
MA
O
R
V'''.splitlines()

WORDS = open('/usr/share/dict/words').read().splitlines()
WORDS = set(w.lower() for w in WORDS if w.isalpha())

def anakey(w):
    w = w.lower()
    w = sorted(w)
    w = ''.join(w)
    return w

def ana_eq(a,b):
    """
    >>> ana_eq('BACON', 'NBACO')
    True
    """
    return anakey(a) == anakey(b)

LETTERS = [chr(ord('a') + x) for x in range(26)]

import itertools
def solve():
    for left, right, add in itertools.product(LEFTS, RIGHTS, LETTERS):
        letters = left + right + add
        for w in WORDS:
            if ana_eq(w, letters):
                print left, right, add, '->', w

if __name__ == '__main__':
    import doctest
    fails, _ = doctest.testmod()
    assert fails == 0
    solve()
