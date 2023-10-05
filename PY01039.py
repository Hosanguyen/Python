def check(s):
    for i in range(0, len(s)-2, 1):
        if(s[i]!=s[i+2]):
            return False
    checked = []
    for i in range(len(s)):
        if s[i] not in checked:
            checked.append(s[i])
            if(len(checked)>2):
                return False
    if(len(checked)!=2):
        return False
    return True
for _ in range(int(input())):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")