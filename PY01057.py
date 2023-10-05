def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)) + 1, 2):
        if(n%i==0):
            return False
    return True
def check(s):
    for i in range(len(s)):
        if (nt(i)):
            if(nt(int(s[i]))==False):
                return False
        else:
            if(nt(int(s[i]))):
                return False
    return True
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")