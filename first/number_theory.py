VALUES = [
    [19, 21, 37, 75, 63],
    [84, 41, 57, 25, 93],
    [32, 20, 11, 12, 23],
    [69, 27, 88, 47, 16],
    [46, 13, 67, 89, 31],
    [29, 45, 51, 73, 39],
    [99, 81, 43, 97, 17]
]

import itertools
from matlib import *

for row in VALUES:
    n = int(''.join([{True: "1", False: "0"}[isprime(k)] for k in row]),
              base=2)
    print n, chr(ord('a') + n - 1)


