def encode(s):
    i = 0
    res = ""
    while(i<len(s)):
        cnt = 1
        j = i+1
        while(j<len(s) and s[j]==s[i]):
            cnt+=1
            j+=1
        res += str(cnt) + str(s[i]) 
        i = j
    return res   
for _ in range(int(input())):
    s = input()
    print(encode(s))