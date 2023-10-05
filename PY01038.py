def sodao(n):
    res = 0
    while(n>0):
        res = res*10 + n%10
        n//=10
    return res
def check(n):
    for _ in range(1001):
        if(n%7==0):
            return n
        n += sodao(n) 
    return -1
for _ in range(int(input())):
    n = int(input())
    print(check(n))