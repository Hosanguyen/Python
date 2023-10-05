for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(0, len(a)-2):
        j = i + 1
        k = len(a)-1
        while (j<k):
            sum = a[i] + a[j] + a[k]
            if sum > 0: k-=1
            if sum < 0: j+=1
            if sum == 0:
                cnt +=1
                j+=1
                k-=1
    print(cnt)