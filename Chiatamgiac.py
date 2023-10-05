import math
for _ in range(int(input())):
    n, h = map(int, input().split())
    hi = 0.0
    for i in range(n-1):
        hi = math.sqrt(h*h/n + hi*hi)
        print(format(hi, "f"), end = ' ')
    print()