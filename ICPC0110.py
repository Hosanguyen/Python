def index_max(a, index1, index2):
    max_index = 0
    while(max_index == index1 or max_index == index2 ):
        max_index+=1
    for i in range(len(a)):
        if(a[i]>a[max_index]):
            if(i!=index1 and i!=index2):
                max_index = i
    return max_index
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    index_max1 = index_max(a, -1, -1)
    #print(index_min1)
    index_max2 = index_max(a, index_max1, -1)
    #print(index_min2)
    index_max3 = index_max(a, index_max1, index_max2)
    #print(index_min3)
    print(a[index_max1] + a[index_max2] + a[index_max3])
