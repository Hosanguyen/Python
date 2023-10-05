for _ in range(int(input())):
    n = int(input())
    check = True
    while(n>0):
        tmp = n%10
        if(tmp!=4 and tmp!=7):
            check = False
            break
        n//=10
    if(check):
        print('YES')
    else:
        print('NO')
    