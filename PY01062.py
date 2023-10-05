def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)), 2):
        if(n%i==0):
            return False
    return True
def check(s):
    if(nt(len(s))==False):
        return False
    nt_cnt = 0
    kont = 0
    for i in range(len(s)):
        if(nt(int(s[i]))):
            nt_cnt+=1
        else:
            kont+=1
    if(kont>=nt_cnt):
        return False
    return True
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")