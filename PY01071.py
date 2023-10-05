s = input()
s = s.lower()
n = len(s)
for i in range(n-1, -1, -1):
    if(s[i] == '.'):
        break
if(i==-1):
    print('no')
else:
    ext = s[i+1:]
    if(ext != 'py'):
        print('no')
    else:
        #s = s.lower()
        check = True
        for i in range(0, i):
            if(s[i].isalpha() == False and s[i] != '.' and s[i]!='_'):
                check = False
                break
        if(check):
            print('yes')
        else:
            print('no')        