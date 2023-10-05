def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)), 2):
        if(n%i==0):
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    x = n % 10000
    if(nt(x)):
        print("YES")
    else:
        print("NO")