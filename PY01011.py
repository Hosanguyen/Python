import queue
import math
def trade(a):
    tmp = a
    while(tmp>0):
        x = tmp%10
        tmp//=10
        a = a*10 +x
    return a
for _ in range(int(input())):
    n = int(input())
    q = queue.Queue()
    q.put(2)
    q.put(4)
    q.put(6)
    q.put(8)
    while(True):
        x = q.get()
        tmp = trade(x)
        if(tmp<n):
            print(tmp, end = ' ')
            q.put(x*10)
            q.put(x*10 + 2)
            q.put(x*10 + 4)
            q.put(x*10 + 6)
            q.put(x*10 + 8)
        else:
            break
    print()    