MAX = int(2e6+5)

def sangnt():
    nt = [True]*(MAX)
    nt[0] = nt[1] = False
    for i in range(2, MAX):
        if(nt[i]):
            for j in range(i*2, MAX, i):
                nt[j] = False
    return nt
nt = sangnt()
res = [0]*(MAX)
for i in range(2, MAX):
    if(nt[i]):
        res[i] = i
    else:
        for j in range(2, int(i**(1/2))+1):
            if(i%j==0):
                res[i] = j + res[i//j]
                break

n = int(input())
sum = 0
for _ in range(n):
    x = int(input())
    sum += res[x]
print(sum)