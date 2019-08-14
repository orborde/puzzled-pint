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
    return f(ERUP) == (f(OUTPUT) // f(MY))

def eq2(f):
    return f(C) == (f(MERCURY) // f(CORRECT))

def solved(f):
    return eq1(f) and eq2(f)

from tqdm import tqdm

for perm in tqdm(itertools.permutations([0,1,3,4,5,6,7,8,9], r=len(ALL_LETTERS_MINUS_C))):
    assignment = {l: i for l,i in zip(ALL_LETTERS_MINUS_C, perm)}

    assert C not in assignment
    assignment[C] = 2

    def mapping(word):
        value = int(''.join(str(assignment[c]) for c in word))
        #print(assignment, word, value)
        return value

    if solved(mapping):
        revmap = {v:k for k,v in assignment.items()}
        phrase = []
        for i in range(10):
            if i in revmap:
                phrase.append(revmap[i])
            else:
                phrase.append('?')
        phrase = ''.join(phrase)

        print(sorted(assignment.items()), phrase)
