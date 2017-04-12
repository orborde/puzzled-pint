MAX = 0b11111
def nt(x):
    """
    >>> bin(nt(0b10101))
    '0b1010'
    """
    r = MAX - x
    assert r >= 0 and r <= MAX
    return r

def decode(x, first=1):
    """
    >>> decode(1)
    'a'
    >>> decode(27)
    '?'
    >>> decode(26)
    'z'
    """
    x -= first
    if x < 0 or x > 25:
        return '?'
    return chr(ord('a') + x)

def decall(v, **kwargs):
    return ''.join(decode(x, **kwargs) for x in v)

import doctest
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

def tryy(data, **kwargs):
    print decall(data, **kwargs)
    print decall(map(nt, data), **kwargs)


if __name__ == '__main__':
    rowdata = [
        0b01101,
        0b10010,
        0b11110,
        0b11110,
        0b11100
    ]
    coldata = [
        0b01111,
        0b10111,
        0b10111,
        0b01110,
        0b10000
    ]
        
    tryy(rowdata)
    tryy(coldata)
