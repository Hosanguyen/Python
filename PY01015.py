def check(s):
    for i in range(1, len(s), 1):
        x = int(s[i])
        y = int(s[i-1])
        if(y>x):
            return False
    return True
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")