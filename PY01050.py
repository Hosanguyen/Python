a = []
for i in range(15):
    a += [0]
check = [0, 0, 0]
n = int(input())
def display():
    for i in range(1, n+1, 1):
        print(chr(a[i] + ord('A')), end = '')
    print()
def hoanvi(i):
    for j in range(3):
        a[i] = j
        check[j]+=1
        if(i==n):
            if(check[0] <= check[1] and check[1] <= check[2]):
                if(check[0]!=0 and check[1]!=0 and check[2]!=0):
                    display()
        else:
            hoanvi(i+1)
        check[j]-=1
x = n
for k in range(3, x+1, 1):
    n = k
    hoanvi(1)
