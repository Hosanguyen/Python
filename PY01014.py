a, k, n = map(int, input().split())
x = a//k
b = k*(x+1) - a
if(b>n-a):
    print(-1)
else:
    while(b<=n-a):
        print(b, end = ' ')
        b+=k