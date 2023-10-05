def tich_chu_so(n):
    if n==0:
        return 0
    tich = 1
    while(n>0):
        x = n%10
        if(x!=0):
            tich *= x
        n//=10
    return tich
for _ in range(int(input())):
    n = int(input())
    print(tich_chu_so(n))