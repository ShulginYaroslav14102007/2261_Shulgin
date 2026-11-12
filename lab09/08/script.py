lst = [1, 'abc', 2, 3, 4, 'aa']

nums = list(filter(lambda x: type(x) == int, lst))

print(nums)