def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

int_max = toint(max)
print(int_max('5', '10', '3'))