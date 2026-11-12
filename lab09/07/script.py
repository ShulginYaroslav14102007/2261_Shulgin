def gen(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    yield 1

def every_other(seq):
    it = iter(seq)
    x = next(it, None)
    while x is not None:
        yield x
        next(it, None)
        x = next(it, None)

print(*gen(7))
print(*every_other([10, 20, 30, 40, 50]))
print(*every_other(range(10)))