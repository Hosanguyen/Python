s = input()
cntUpper = 0
cntLower = 0
for i in range(len(s)):
    if(ord(s[i]) >= 97):cntLower+=1
    else: cntUpper+=1
if(cntLower>=cntUpper):
    print(s.lower())
else:
    print(s.upper())