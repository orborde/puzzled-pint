FRAGMENTS="""
ACCE
ARD
BA
BARBA
BL
CHES
CKET
COLL
COLO
COM
DE
ECTOR

EN
ER
ER
EXP
GE
GR
IAN
IDER
IST
LEO
M
M

MI
ND
NSE
OCK
ON
COURAGE
PAD
R
RRY
RSHIP
S
SSAGE

STA
SWE
T
TED
TSHOP
UTER
VE
W
WA
WA""".strip().split()

COUNTS = [
    16,
    10,
    12,
    14,
    10,
    12,
    14,
    14,
    16,
    14,
    18,
    18,
    18,
    12,
    10,
    10,
    14,
    16,
    16,
    14,
    12,
    14,
    10,
]

WORDS = open('/usr/share/dict/words').read().split()
WORDS = filter(lambda s: s.isalpha(), WORDS)
WORDS = set(w.upper() for w in WORDS)

print len(WORDS), 'words'

PREFIXES = set()
for w in WORDS:
    for i in range(1, len(w)+1):
        prefix = w[:i]
        PREFIXES.add(prefix)
print len(PREFIXES), 'prefixes'

assert(all(f.isalpha()) for f in FRAGMENTS)
print sum(len(f) for f in FRAGMENTS), 'total fragment letters'
assert len(COUNTS) == 23
print sum(COUNTS), 'blanks',
print '(',sum(COUNTS) - sum(len(f) for f in FRAGMENTS), 'vs fragments)'
print  '/2 =', sum(COUNTS)/2, sum(COUNTS)/2 - sum(len(f) for f in FRAGMENTS)

def findwords(prefix='', fragments=FRAGMENTS):
    if prefix in WORDS:
        yield prefix

    for i in range(len(fragments)):
        f = fragments[i]
        word = prefix + f
        if word not in PREFIXES:
            continue
        new_frags = fragments[:i] + fragments[i+1:]
        assert len(new_frags) == len(fragments) - 1
        for w in findwords(word, new_frags):
            yield w

findables = list(findwords())
print len(findables), 'findable words found'

import collections
by_lengths = collections.defaultdict(list)
for word in findables:
    by_lengths[len(word)].append(word)

#for length, words in by_lengths.iteritems():
#    print length, ' '.join(sorted(set(words)))

# ha ha i had it totally wrong
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert len(LETTERS) == 26
import itertools
pair_sets = {}
for left, right in itertools.permutations(FRAGMENTS, r=2):
    if (left,right) in pair_sets:
        print '...dropping', left,right
        continue
    words = []
    for middle in LETTERS:
        word = left+middle+right
        print left,middle,right,word,
        if word in WORDS:
            print 'YES',
            words.append(word)
            print words,
        print
    if len(words) >= 2:
        key = left,right
        assert key not in pair_sets
        print 'stick in', words
        pair_sets[key] = words

for i in range(1,10):
    print i
    for left,right in pair_sets.iterkeys():
        if len(left)+len(right)+1 == i:
            print ' '.join(set(pair_sets[left,right]))
    print

