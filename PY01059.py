for _ in range(int(input())):
    s = input()
    tong = 0
    tich = 1
    check = False
    for i in range(len(s)):
        if(i%2==0):
            tong += int(s[i])
        else:
            if(s[i]!='0'):
                check = True
                tich *= int(s[i])
    if(check==False):
        tich = 0
    print(tong, tich)
