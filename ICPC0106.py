import math 
def trade(a):
    digit = 0
    for i in range(len(a)-1, -1, -1):
        digit += a[i]*2**(len(a)-i-1)
    return digit
for _ in range(int(input())):
    b = int(input())
    b = int(math.log(b, 2))
    #print(b)
    s = input()
    res = ""
    for i in range(len(s)-1, -1, -b):
        a = []
        for j in range(i, i-b, -1):
            if j > -1: a = [int(s[j])] + a
        #while(len(a)<b): a = [0] + a
        #print(a)
        #print(trade(a))
        tmp = trade(a)
        if tmp >10:
            res += chr(tmp+55)
        else: 
            res += str(tmp)
        #print(res)
    res = res[::-1]
    print(res)