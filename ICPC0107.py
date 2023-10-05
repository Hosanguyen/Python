def tong_max(x, y, p, q):
    return int( x.replace(str(q), str(p)) ) + int( y.replace(str(q), str(p)) )
def tong_min(x, y, p, q):
    return int( x.replace(str(p), str(q)) ) + int( y.replace(str(p), str(q)) )
for _ in range(int(input())):
    p, q = map(int, input().split())
    x = input()
    tmp = list(map(str, x.split() ))
    #print(tmp)
    if len(tmp)==2:
        x, y = tmp[0], tmp[1]
    else: y = input()
    if p < q: p, q = q, p
    print(tong_min(x, y, p, q), tong_max(x, y, p, q))