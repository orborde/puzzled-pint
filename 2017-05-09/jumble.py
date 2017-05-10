WORDS = open('/usr/share/dict/words').read().splitlines()
WORDS = set(w.lower() for w in WORDS if w.isalpha())

PATTERN = [
    'CDHDH',
    'HCHC',
    'HDDCCD',
]

LETTERPILES = {
    'C': 'crrto',
    'H': 'uosyh',
    'D': 'sears'
}

assert (sum(len(v) for v in LETTERPILES.values()) ==
        sum(len(w) for w in PATTERN))

import itertools

def assign(piles):
    words = []
    pos = {'C':0, 'H':0, 'D':0}
    for w in PATTERN:
        word = []
        for c in w:
            idx = pos[c]
            pos[c] += 1
            l = piles[c][idx]
            word.append(l)
        word = ''.join(word)
        words.append(word)
    return words

for c in itertools.permutations(LETTERPILES['C']):
    for h in itertools.permutations(LETTERPILES['H']):
        for d in itertools.permutations(LETTERPILES['D']):
            piles = {
                'C': ''.join(c),
                'H': ''.join(h),
                'D': ''.join(d)
            }
            words = assign(piles)
            if all(w in WORDS for w in words):
                print ' '.join(words).upper()
