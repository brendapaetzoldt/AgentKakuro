import bisect
import os.path
import random
import math
from re import I


def soma(seq):
    return sum(bool(x) for x in seq)

def primeira(i, default=None):
    try:
        return i[0]
    except IndexError:
        return default
    except TypeError:
        return next(i, default)

def is_in(elt, seq):
    return any(x is elt for x in seq)

id = lambda x: x
argmin = min
argmax = max

def argMin(seq, key=id):
    return argmin(embaralhar(seq), key=key)

def argmax_random_tie(seq, key=id):
    return argmax(embaralhar(seq), key=key)

def embaralhar(i):
    items = list(i)
    random.shuffle(items)
    return items

def probabilidade(p):
    return p > random.uniform(0.0, 1.0)

def SubAmostraPonderada(seq, pesos, n):
    sample = amostraPonderada(seq, pesos)
    return [sample() for _ in range(n)]

def amostraPonderada(seq, pesos):
    totals = []
    for w in pesos:
        totals.append(w + totals[-1] if totals else w)
    return lambda: seq[bisect.bisect(totals, random.uniform(0, totals[-1]))]

def memorizar(fn, slot=None):
    if slot:
        def memorizado(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memorizado(*args):
            if args not in memorizado.cache:
                memorizado.cache[args] = fn(*args)
            return memorizado.cache[args]
        memorizado.cache = {}
    return memorizado

def nome(obj):
    return (getattr(obj, 'name', 0) or getattr(obj, '__name__', 0) or
            getattr(getattr(obj, '__class__', 0), '__name__', 0) or
            str(obj))

def isNumero(x):
    return hasattr(x, '__int__')

def tabela(table, header=None, sep='   ', numfmt='%g'):
    justs = ['rjust' if isNumero(x) else 'ljust' for x in table[0]]
    if header:
        table.insert(0, header)
    table = [[numfmt.format(x) if isNumero(x) else x for x in row]
             for row in table]
    sizes = list(
            map(lambda seq: max(map(len, seq)),
                list(zip(*[map(str, row) for row in table]))))
    for row in table:
        print(sep.join(getattr(
            str(x), j)(size) for (j, size, x) in zip(justs, sizes, row)))


def file(components, mode='r'):
    aima_root = os.path.dirname(__file__)
    aima_file = os.path.join(aima_root, *components)
    return open(aima_file)

def DataFile(name, mode='r'):
    return file(['aima-data', name], mode)

class Expr(object):
    def __init__(self, op, *args):
        self.op = str(op)
        self.args = args

class Fila:
    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)

def Stack():
    return []

class Fifo(Fila):
    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A) / 2:
            self.A = self.A[self.start:]
            self.start = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.start:]

class PrioridadeFila(Fila):
    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.A)

    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)