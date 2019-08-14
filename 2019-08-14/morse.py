#! /usr/bin/env python3

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def morse(word):
    word = word.upper()
    return ''.join(MORSE_CODE_DICT[c] for c in word)

LETTERS=set('QWERTYUIOPASDFGHJKLZXCVBNM')
assert len(LETTERS) == 26
def isletters(word):
    return all(c.upper() in LETTERS for c in word)

WORDS = open('/usr/share/dict/words').read().split()
WORDS = filter(isletters, WORDS)
WORDS = [w for w in WORDS if len(w) > 1 and w.lower() == w]
WORDS.append('a')
WORDS = set(w.upper() for w in WORDS)
WORDS = sorted(WORDS, key=lambda w: len(morse(w)), reverse=True)
WORD2MORSE = {word: morse(word) for word in WORDS}

def morsedec(sequence):
    if sequence == '':
        yield []
        return

    for w in WORDS:
        m = WORD2MORSE[w]

        if not sequence.startswith(m):
            continue

        rest = sequence[len(m):]
        #print('--', w, m, rest)
        for decode in morsedec(rest):
            yield [w] + decode

if __name__ == '__main__':
    crypt = '...---.-..-.-.---.-----..-'+'-..'+'..'+'.'+'-..'
    for dec in morsedec(crypt):
        assert all(w.upper() in WORDS for w in dec)
        assert ''.join(morse(w) for w in dec) == crypt
        print(dec)
