def index_min(a, index1, index2):
    min_index = 0
    for i in range(len(a)):
        if(a[i]<a[min_index]):
            if(i!=index1 and i!=index2):
                min_index = i
    return min_index
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    index_min1 = index_min(a, -1, -1)
    #print(index_min1)
    index_min2 = index_min(a, index_min1, -1)
    #print(index_min2)
    index_min3 = index_min(a, index_min1, index_min2)
    #print(index_min3)
    print(a[index_min1] + a[index_min2] + a[index_min3])
