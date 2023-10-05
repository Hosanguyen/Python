def nt(n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2))+1, 2):
        if(n%i==0):
            return False
    return True
def check(s):
    sum = 0
    for i in range(len(s)):
        if(int(s[i])%2!=i%2):
            return False
        sum += int(s[i])
    return nt(sum)
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
        