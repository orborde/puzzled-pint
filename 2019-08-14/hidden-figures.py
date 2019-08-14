#! /usr/bin/env python3

import itertools

ERUP='ERUP'
MY='MY'
OUTPUT='OUTPUT'
CORRECT='CORRECT'
C='C'
MERCURY='MERCURY'

ALL_WORDS = [ERUP, MY, OUTPUT, CORRECT, C, MERCURY]
ALL_LETTERS = set()
for w in ALL_WORDS:
    for c in w:
        ALL_LETTERS.add(c)

ALL_LETTERS_MINUS_C = sorted(ALL_LETTERS.difference(set(C)))
print(len(ALL_LETTERS_MINUS_C))

def eq1(f):
    return f(ERUP) * f(MY) == f(OUTPUT)

def eq2(f):
    return f(CORRECT) * f(C) == f(MERCURY)

def solved(f):
    return eq1(f) and eq2(f)

from tqdm import tqdm

for perm in tqdm(itertools.product(range(10), repeat=len(ALL_LETTERS_MINUS_C))):
    assignment = {l: i for l,i in zip(ALL_LETTERS_MINUS_C, perm)}

    assert C not in assignment
    assignment[C] = 2

    def mapping(word):
        value = int(''.join(str(assignment[c]) for c in word))
        #print(assignment, word, value)
        return value

    if solved(mapping):
        print(sorted(assignment.items()))
