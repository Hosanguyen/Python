for _ in range(int(input())):
    s = input()
    tmp = s[0:2]
    x = int(tmp)
    tmp = s[len(s)-2:len(s)]
    y = int(tmp)
    if(x==y):
        print("YES")
    else:
        print("NO")