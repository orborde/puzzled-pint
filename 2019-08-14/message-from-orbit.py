#!/usr/bin/env python3

import morse

def unfold(r):
    if len(r) == 0:
        yield ''
        return

    first, rest = r[0], r[1:]

    if first == 'X':
        fp = '.-'
    else:
        fp = first

    for p in fp:
        for suf in unfold(rest):
            yield p+suf

basemap={
    1: '.-',
    2: '-.',
    3: 'XX',
    4: 'X.',
    5: '--',
    6: '-X',
    7: '..',
    8: '.X',
    9: 'XX',
}

foldmap = {n: list(unfold(v)) for n,v in basemap.items()}

numbers = sorted(foldmap.keys())
possibles = [foldmap[n] for n in numbers]

initialcrypt = '54474746588418185653561827486'
finalcrypt=(
    '25954142319878168'
    '184878978881248292'
)

initialmorse=''.join(basemap[int(q)] for q in initialcrypt)

import itertools
for sequence in unfold(initialmorse):
    printed=False
    for dec in morse.morsedec(sequence):
        if not printed:
            print(sequence)
            printed=True

        print(dec)
