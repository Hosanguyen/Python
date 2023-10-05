def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)), 2):
        if(n%i==0):
            return False
    return True
def tong_chu_so(n):
    res = 0
    while(n>0):
        res += n%10
        n//=10
    return res
for _ in range(int(input())):
    n = int(input())
    if(nt(tong_chu_so(n))):
        print("YES")
    else:   
        print("NO")