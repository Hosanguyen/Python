n = int(input())
a = list(map(int, input().split()))
cnt = len(a)
if(len(a)>1):
    j = 0
    i = 1
    while(i<len(a)):
        if((a[i] + a[j])%2==0):
            cnt-=2
            if(j==0):
                j = i + 1
                i += 2
            else:
                j-=1
                i+=1
        else:
            j = i
            i += 1
print(cnt)