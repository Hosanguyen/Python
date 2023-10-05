def Rotate(s):
    vr = 0 # gia tri xoay
    for i in s:
        vr += ord(i) - ord('A')
    vr %= 26
    res = ""
    for i in range(len(s)):
        cnt = ord(s[i]) - ord('A') + vr
        if(cnt>25):
            cnt-=26
        res += chr(cnt + ord('A'))
    return res
def Merge(a, b):
    res = ""
    for i in range(len(a)):
        cnt = ord(a[i]) - ord('A') + ord(b[i]) - ord('A')
        if(cnt>25):
            cnt-=26
        res += chr(cnt + ord('A'))
    return res

for _ in range(int(input())):
    s = input() 
    n = len(s)
    a = s[0:int(n/2)]
    b = s[int(n/2):n]
    a = Rotate(a)
    b = Rotate(b)
    print(Merge(a, b))
