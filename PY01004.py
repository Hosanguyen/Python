import math
def sont(n):
    if(n<2):return False
    if(n==2 | n==5):return True
    if(n%2==0): return False
    for i in range(3, math.sqrt(n), 2):
        if(n%i==0):
            return False
    return True
def gcd(a, b):
    if(b==0):return a
    return gcd(b, a%b)
for _ in range(int(input())):
    n = int(input())
    if(n==1):
        print("NO")
    else:
        k = 0
        for i in range(1, n):
            if(gcd(n, i)==1):
                k+=1
        if(sont(k)):
            print("YES")
        else:
            print("NO")