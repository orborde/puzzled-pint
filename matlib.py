import itertools
import math
import time

# HELLO FUTURE WILLIAM
#
# THIS IS PAST WILLIAM
#
# I HAVE PEERED INTO THE EVEN DEEPER PAST SO THAT YOU DO NOT HAVE TO
#
# THIS CLASS EXISTS BECAUSE XRANGE REFUSES TO TAKE NON-INT ARGUMENTS
#
# PROBABLY
class yrange:
    def __init__(self, min, max, step=1):
        self.min, self.max, self.step = min,max,step
        self.cur=min

    def __iter__(self):
        return self

    def next(self):
        z=self.cur
        self.cur += self.step
        if self.cur < self.max:
            return z
        else:
            raise StopIteration

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for z in xrange(2,int(math.ceil(math.sqrt(n))+1)):
        if (n%z) == 0:
            return False
    return True

# This might be doable more efficiently, but it's easy so far.
def factor(n, lb=2):
    for z in yrange(lb,math.sqrt(n)+1):
        #print n,z
        r = n % z
        if r == 0:
            return [z] + factor(n/z, lb=z)
    return [n]

def prime_factor(n):
    for z in itertools.chain([2], yrange(3,math.sqrt(n)+1,2)):
        r = n % z
        if r == 0:
            return [z] + prime_factor(n/z)
    return [n]

# Returns all the integer divisors of a number
def divisors(n):
    dd=set()
    ssq = int(math.ceil(math.sqrt(n)))
    for i in xrange(1,ssq+1):
        if (n % i) == 0:
            dd.add(i)
            dd.add(n/i)
    return list(dd)

# Returns a dictionary keyed by factor of the power to which that factor is raised
def powfact(n):
    d={1:1}
    for i in factor(n):
        if i == 1:
            continue
        if i not in d:
            d[i]=0
        d[i] += 1

    return d

# Merges two powfact structs into a third
def merge_powfact(a,b):
    c={}
    kk=set(a.keys() + b.keys())
    for k in kk:
        if not k in a:
            c[k]=b[k]
            continue
        if not k in b:
            c[k]=a[k]
            continue
        c[k] = max(a[k],b[k])

    return c

def lcm(*a):
    # ONE LINER FOR VICTORY
    # Also bugs. BUGGY BUGGY BUGGY - try 6,4 -> 24?!
    return product(map(lambda t: t[0]**t[1], reduce(merge_powfact, map(powfact,a)).iteritems()))

def product(seq):
    return reduce(lambda a,b: a*b, seq)

# Do this the RIGHT darned way...
def primegen():
    cur = 1
    factors=[]
    while True:
        cur += 1
        ssq=int(math.sqrt(cur) + 1)
        while anyfilt(lambda f: cur%f == 0,
                      inhale(lambda f: f <= ssq,
                             factors)):
            cur += 1
            ssq=int(math.sqrt(cur) + 1)
        factors.append(cur)
        yield cur

def anyfilt(func, seq):
    for e in seq:
        if func(e):
            return True
    return False

def inhale(cont, itr):
    l=[]
    for e in itr:
        if not cont(e):
            return l
        l.append(e)
    return l

class iterseq:
    def __init__(self, itr):
        self.itr = itr
        self.vals=[]

    def __getitem__(self, key):
        while len(self.vals) <= key:
            self.vals.append(self.itr.next())
            #print len(self.vals)
        return self.vals[key]

def primes():
    return iterseq(primegen())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n,r):
    return factorial(n)/ (factorial(r) * factorial(n - r))

def nPr(n,r):
    return factorial(n)/factorial(n - r)


def argmax(evaluator, argseq):
    best = float('-inf')
    bestarg = None
    for aq in argseq:
        val = evaluator(*aq)
        if val > best:
            best = val
            bestarg = aq
    return bestarg


def numberize(seq):
    """
    >>> numberize((3,5,2))
    352
    """
    s = 0
    for d in seq:
        s *= 10
        s += d
    return s


if __name__=='__main__':
    print inhale(lambda n: n<100, primegen())
    print primes()[10]
    start=time.time()
    l=primes()[30000]
    end=time.time()
    print 'Prime',l,'found in',end-start,'seconds'
