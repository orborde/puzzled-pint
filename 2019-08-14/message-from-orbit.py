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

crypt=(
    '25954142319878168'
    '184878978881248292'
)

import itertools
for assignment in itertools.product(*possibles):
    assignment = {n:v for n,v in zip(numbers, assignment)}
    sequence = ''.join(assignment[int(q)] for q in crypt)

    printed=False
    for dec in morse.morsedec(sequence):
        if not printed:
            print(assignment)
            printed=True

        print(dec)
