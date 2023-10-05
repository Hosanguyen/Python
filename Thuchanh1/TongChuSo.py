def tong(s):
    sum = 0
    i = 0
    if(s[0]=='-'):
        sum = int(s[0:2])
        i = 2
    while(i<len(s)):
        sum += int(s[i])
        i+=1
    return str(sum)

s = input()
res = 0
while(True):
    if(len(s)==1):
        break
    if(int(s)<0 and len(s)==2):
        break
    s = tong(s)
    res+=1
print(res)