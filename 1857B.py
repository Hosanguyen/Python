for _ in range(int(input())):
    s = input()
    idx = len(s)
    memory = 0
    for i in range(len(s)-1, -1, -1):
        tmp = int(s[i])
       # print(tmp)
        tmp += memory
        if tmp>=10:
            memory = 1
            tmp%=10
            #s[i] = str(tmp)
        elif tmp >=5:
            memory = 1
            tmp = 0
            idx-=1
            #s[i] = str(tmp)
        else:
            memory = 0
    for i in range(0, idx+1):
        print(s[i], end = '')
    for i in range(idx+1, len(s)):
        print(0, end = '')
            