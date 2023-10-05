def check(s):
    if(len(s)<3):
        return False
    i = 0
    while(i<len(s)-1 and s[i]<s[i+1]):
        i+=1
    while(i<len(s)-1 and s[i]>s[i+1]):
        i+=1
    if(i!=len(s)-1):
        return False
    return True
for _ in range(int(input())):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")