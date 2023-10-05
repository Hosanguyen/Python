for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        dic[a[i]] = c[i]
    key =sorted(dic)
    print(key)