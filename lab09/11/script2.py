def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

int_min = toint(min)
print(int_min('5', '10', '3'))