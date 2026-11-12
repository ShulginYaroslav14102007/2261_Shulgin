def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

int_pow = toint(pow)
print(int_pow('2', '3'))