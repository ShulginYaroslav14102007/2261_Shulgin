a = list(range(10))
b = [a.pop() for _ in a]
print(b)
print(a)