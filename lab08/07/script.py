x = [int(t) for t in input().split()]

for num in x:
    if num < 0:
        print(num)
        break
else:
    print("No negative numbers")