import math
def sont(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(math.sqrt(n)), 2):
        if(n%i==0):
            return False
    return True
def ucln(a, b):
    if(b==0):
        return a
    return ucln(b, a%b)
def tong_chu_so(a):
    res = 0
    while(a>0):
        res += a%10
        a//=10
    return res
for _ in range(int(input())):
    a, b = map(int, input().split())
    tong = tong_chu_so(ucln(a, b))
    if(sont(tong)):
        print("YES")
    else:
        print("NO")