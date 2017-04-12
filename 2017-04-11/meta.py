C='C'
D='D'
H='H'
S='S'

J='J'
Q='Q'
K='K'

CARDS = [
    (2, C, 'L'),
    (3, C, 'E'),
    (4, C, 'F'),
    (Q, C, 'T'),

    (K, D, 'H'),
    (9, D, 'U'),
    (J, D, 'N'),
    (5, D, 'T'),

    (6, H, 'F'),
    (10, H, 'I'),
    (4, H, 'S'),
    (7, H, 'H'),

    (5, S, 'S'),
    (3, S, 'O'),
    (8, S, 'L'),
    (10, S, 'E'),
]

import collections
Card = collections.namedtuple(
    'Card',
    ['rank', 'suit', 'letter'])

CARDS = [
    Card(rank=rank, suit=suit, letter=letter)
    for rank, suit, letter in CARDS]

def unique(arr):
    return len(set(arr)) == len(arr)

def part1(hands):
    if not all(len(h) <= 4 for h in hands):
        return False

    return all(unique([c.rank for c in hand]) for hand in hands)

def full1(hands):
    if not all(len(h) == 4 for h in hands):
        return False

    return all(unique([c.rank for c in hand]) for hand in hands)

def part2(hands):
    return (unique([c.suit for c in hands[0]]) and
            unique([c.suit for c in hands[2]]))

def full2(hands):
    return (
        part2(hands) and
        (not unique([c.suit for c in hands[1]])) and
        (not unique([c.suit for c in hands[3]])))
