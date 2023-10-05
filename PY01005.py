n = int(input())
cnt = 0
while(n>0):
    tmp = n%10
    n//=10
    if(tmp == 4 or tmp == 7):
        cnt+=1
if(cnt == 4 or cnt == 7):
    print('YES')
else:
    print('NO')