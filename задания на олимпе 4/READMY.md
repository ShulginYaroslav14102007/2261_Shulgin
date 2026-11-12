### 1 задание
```
n = int(input())

count = 0
num = 2

while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        count += 1
        
    if count == n:
        print(num)
        break
        
    num += 1
```



### 2 задание

```
n = int(input())
dresses = list(map(int, input().split()))

seen = set()

for i in range(n):
    seen.add(dresses[i])
    if len(seen) == 3:
        print(i + 1)
        break
else:
    print(n)
```



### 3

```
from string import ascii_lowercase

s = input()

max_count = 0
best_letter = ''

for letter in ascii_lowercase:
    count = s.count(letter)
    if count > max_count:
        max_count = count
        best_letter = letter

result = s.replace(best_letter, '')

print(result)
```



### 4 задание

```
n = int(input())

row1 = "1234567890"
row2 = "qwertyuiop"
row3 = "asdfghjkl"
row4 = "zxcvbnm"

for _ in range(n):
    password = input()
    
    has1 = False
    has2 = False
    has3 = False
    has4 = False
    
    for char in password:
        if char in row1:
            has1 = True
        if char in row2:
            has2 = True
        if char in row3:
            has3 = True
        if char in row4:
            has4 = True
            
    if has1 and has2 and has3 and has4:
        print("strong")
    else:
        print("weak")
```



### 5 задание

```
ranks = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
rank_value = {r: i for i, r in enumerate(ranks)}

trump = input().strip()
n = int(input())

results = []
for _ in range(n):
    attack_rank, attack_suit = input().split()
    beat_rank, beat_suit = input().split()

    beats = False
    if attack_suit == beat_suit:
        beats = rank_value[beat_rank] > rank_value[attack_rank]
    elif beat_suit == trump and attack_suit != trump:
        beats = True

    results.append('1' if beats else '0')

print(' '.join(results))
```