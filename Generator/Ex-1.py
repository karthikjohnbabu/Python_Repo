def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g= mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))#StopIteration run time error.