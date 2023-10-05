def encode(s, k):
    res = ""
    for i in range(len(s)):
        code = 0
        if(s[i] == '_'):
            code = 26
        elif(s[i] == '.'):
            code = 27
        else:
            code = ord(s[i])-65
        x = (code+k)%28
        res = P[x] + res
    return res
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while(True):
    tmp = list(map(str, input().split()))
    if(len(tmp)==1):
        break
    k = int(tmp[0])
    s = tmp[1]
    print(encode(s, k))