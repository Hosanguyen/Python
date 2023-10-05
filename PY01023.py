import math
def phantichthuasonguyento(n):
    res = "1"
    for i in range (2, n+1, 1):
        if(n%i==0):
            cnt = 0
            while(n%i==0):
                cnt+=1
                n//=i
            res += " * " + str(i) + "^" + str(cnt)
    print(res)
for _ in range(int(input())):
    n = int(input())
    phantichthuasonguyento(n)