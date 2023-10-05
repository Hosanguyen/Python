for _ in range(int(input())):
    m, n = map(int, input().split())
    List = []
    tong = 0
    trung = 0
    for i in range(m):
        tmp = list(map(int, input().split()))
        List.append(tmp)
    for i in range(0, len(List[0])):
        tong += List[0][i]
        trung += max(List[0][i]-1, 0)
        if(i<len(List[0])-1):
            trung += min(List[0][i], List[0][i+1])
    for i in range(1, len(List)):
        for j in range(0, len(List[i])):
            tong += List[i][j]
            trung += max(List[i][j]-1, 0)
            if(j<len(List[i])-1):
                trung += min(List[i][j], List[i][j+1])
            trung += min(List[i-1][j], List[i][j])
    print(tong*6 - trung*2)