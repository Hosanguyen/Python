for _ in range(int(input())):
    a, b, x, y, z, l, r = map(int, input().split())
    V = []
    for h in range(2, min(a, b), 2):
        v = (a-h)*(b-h)*(h//2)
        V.append(v)
    V.sort()
    V = V[::-1]
    for x1 in range((l-x)//V[0], (r-x)//V[0]+1):
        n = V[0]*x1+x
        if((n-y)%V[1]==0 and (n-z)%V[2]==0):
            print(n)
            break
