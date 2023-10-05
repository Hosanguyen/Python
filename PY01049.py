def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)), 2):
        if(n%i==0):
            return False
    return True
def check(n):
    sum = 0
    cnt_nt = 0
    cnt_not = 0
    while(n>0):
        x = n%10
        if(nt(x)):
            cnt_nt+=1
        else:
            cnt_not+=1
        sum += 1
        n//=10
    if(nt(sum)==False):
        return False
    if(cnt_nt <= cnt_not):
        return False
    return True
for _ in range(int(input())):
    n = int(input())
    if(check(n)):
        print("YES")
    else:
        print("NO")