"""
Tema5 - 30% din nota finala
Moditicati acest iterator astfel incat sa genereze urmatorul numar prim doar atunci cand
este apelata functia next() pe obiectul de tip 'PrimesIter' si nu toate numerele prime atunci cand se instantiaza
Aveti un indiciu cu o geseala mai jos si va trebui sa modificati si constructorul
"""

from time import time


class PrimesIter():

    def __init__(self, max_prime):
        self.max_prime = max_prime
        self.start = 1

    def __next__(self):
        for x in range(self.start, self.max_prime):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                self.start = x + 1
                return x
        else:
            raise StopIteration

    def __iter__(self):
        return self


start = time()
prime = PrimesIter(30000)
stop = time()
assert (stop < start + 1)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))