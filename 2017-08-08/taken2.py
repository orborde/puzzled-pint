import itertools

SECTIONS="""
NR
EA
OA
DL
AE
IS
PT
AO
ET
AE
TC
DR
EA
PN
SX
FG
AE
NR
MP
OA
NP
AE
CR
""".strip().split()

WORDS = open('/usr/share/dict/words').read().split()
WORDS = filter(lambda s: len(s) > 1 and s.isalpha() and s.islower(), WORDS)
WORDS.append('a')
WORDS = set(w.upper() for w in WORDS)

print len(WORDS), 'words'

PREFIXES = set()
for w in WORDS:
    for i in range(1, len(w)+1):
        prefix = w[:i]
        PREFIXES.add(prefix)
print len(PREFIXES), 'prefixes'

def extend(new_words, section):
    prefix, last = new_words[:-1], new_words[-1]
    for c in SECTIONS[section]:
        newlast = last + c
        for soln in sentences(prefix + [newlast], section+1):
            yield soln

def sentences(words=[''], section=0):
    prefix, last = words[:-1], words[-1]
    if len(last) > 0 and last not in PREFIXES:
        return

    if section == len(SECTIONS):
        if all(w in WORDS for w in words):
            yield ' '.join(words)
        return

    successors = [extend(words, section)]
    if last in WORDS:
        successors.append(extend(prefix + [last, ''], section))
    for soln in itertools.chain(*successors):
        yield soln

solns = list(sentences())
for s in solns:
    print s
print len(solns), 'solutions found'

