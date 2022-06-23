import random
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

id = lambda x: x
argmin = min
argmax = max

def argMin(seq, key=id):
    return argmin(embaralhar(seq), key=key)

def embaralhar(i):
    items = list(i)
    random.shuffle(items)
    return items

class Fila:
    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)

def Stack():
    return []