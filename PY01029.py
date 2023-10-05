def sodao(n):
    res = 0
    while(n>0):
        res = res*10 + n%10
        n//=10
    return res
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
for i in range(int(input())):
    n = int(input())
    if(ucln(n, sodao(n))==1):
        print("YES")
    else:
        print("NO")