import math as m

# tim uoc chung lon nhat
def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)

n, k = map(int, input().split())
start = 10**(k-1)
end = 0
for i in range(k):
    end = end*10 + 9
cnt = 0
for i in range(start, end+1, 1):
    if(gcd(n, i)==1):
        print(i, end = ' ')
        cnt+=1
    if(cnt==10):
        print()
        cnt = 0