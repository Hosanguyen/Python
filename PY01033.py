# tim uoc chung lon nhat
def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)

#xac dinh bo 3 so nguyen to cung nhau
def bo_3_nguyento(a, b, c):
    if(gcd(a, b)!=1):
        return False
    if(gcd(a, c)!=1):
        return False
    if(gcd(b, c)!=1):
        return False
    return True
l, r = map(int, input().split())
for i in range(l, r-1, 1):
    for j in range(i+1, r, 1):
        for k in range(j+1, r+1, 1):
            if(bo_3_nguyento(i, j, k)):
                print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")
