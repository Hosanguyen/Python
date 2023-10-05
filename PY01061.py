def nt (n):
    if(n==2):
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3, int(n**(1/2)), 2):
        if(n%i==0):
            return False
    return True
for _ in range(int(input())):
    s = input()
    #print(s[0:3], s[len(s)-3:len(s)])
    if(nt(int(s[0:3])) and nt(int(s[len(s)-3:len(s)]))):
        print("YES")
    else:
        print("NO")
