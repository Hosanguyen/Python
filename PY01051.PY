def so_dao(n):
    res = 0
    while(n>0):
        res = res*10 + n%10
        n//=10
    return res
def tong_chu_so(n):
    sum = 0
    while(n>0):
        sum += n%10
        n//=10
    return sum
for _ in range(int(input())):
    n = int(input())
    a = tong_chu_so(n)
    b = so_dao(a)
    if(a==b and len(str(a))>1):
        print("YES")
    else:
        print("NO")