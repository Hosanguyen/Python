import math
for _ in range(int(input())):
    n, x, m = map(float, input().split())
    res = int( math.log(m/n, 1 + x/100) + 1)
    print(res)