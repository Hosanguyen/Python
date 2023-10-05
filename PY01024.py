def check(n):
    sum = 0
    sau = n%10
    n//=10
    sum += sau
    while(n>0):
        truoc = n%10
        n//=10
        if(abs(truoc-sau)!=2):
            return False
        sau = truoc
        sum += truoc
    if(sum%10!=0):
        return False
    return True
for _ in range(int(input())):
    n = int(input())
    if(check(n)):
        print('YES')
    else:
        print("NO")