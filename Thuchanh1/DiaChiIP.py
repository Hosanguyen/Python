def check(s):
    cnt = 0
    for i in s:
        if(i=='.'): 
            cnt+=1
    if(cnt!=3):
        return False
    if(s[0]=='.' or s[len(s)-1]=='.'):
        return False
    for i in s:
        if(i=='.'):continue
        if(i<'0' or i > '9'):
            return False
    a = list(map(int, s.split('.')))
    for x in a:
        if(x<0):
            return False
        if(x>255):
            return False
    return True
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")

