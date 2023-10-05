def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2))+1, 2):
        if(n%i==0):
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    if(nt(n%10000)):
        print("YES")
    else:
        print("NO")