from itertools import permutations

s = input()

words = [''.join(p) for p in permutations(s)]

for x in words:
    print(x)