
def check(s):
    daos = s[::-1]
    if(len(s)==1):
        return True
    for i in range(0, len(s)-1):
        if(abs(ord(s[i+1])-ord(s[i]))!= abs(ord(daos[i+1]) - ord(daos[i]))):
            return False
    return True

for _ in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
