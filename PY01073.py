s = input()
x = []
check = []
n = len(s)
for i in range(n+1):
    x += [0]
    check += [False]
def display():
    for i in range(1, n+1):
        print(s[x[i]-1], end = '')
    print()
def hoanvi(i):
    for j in range(1, n+1):
        if(check[j]==False):
            x[i] = j
            check[j] = True
            if(i==n):
                display()
            else:
                hoanvi(i+1)
            check[j] = False

hoanvi(1)