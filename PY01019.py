import math
def xaudao(s):
    return s[::-1]
def check(s):
    st = xaudao(s)
    for i in range(1, len(s)):
        if(abs(ord(s[i]) - ord(s[i-1])) != abs(ord(st[i]) - ord(st[i-1]))):
            return False
    return True
for _ in range(int(input())):
    s = input()
    if(check(s)):
        print('YES')
    else:
        print('NO')