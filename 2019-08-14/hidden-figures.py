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

ALL_LETTERS_MINUS = sorted(ALL_LETTERS.difference(set('CB')))
print(len(ALL_LETTERS_MINUS))

def eq1(f):
    return f(ERUP) == (f(OUTPUT) // f(MY))

def eq2(f):
    return f(C) == (f(MERCURY) // f(CORRECT))

def solved(f):
    return eq1(f) and eq2(f)

from tqdm import tqdm

for perm in itertools.permutations([0,1,3,4,5,6,7,8,9], r=len(ALL_LETTERS_MINUS)):
    assignment = {l: i for l,i in zip(ALL_LETTERS_MINUS, perm)}

    assert C not in assignment
    assignment[C] = 2
    assert 'B' not in assignment
    assignment['B'] = 0

    #print(assignment)

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

        vv = 51*mapping('CUBE') + (17 * mapping('ROOT')) - mapping('YUM')
        answer = []
        for digit in str(vv):
            answer.append(revmap[int(digit)])
        answer = ''.join(answer)

        print(phrase, answer)
