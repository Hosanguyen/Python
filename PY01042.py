def base_three(s):
    checked = ['0', '1', '2']
    for i in range(len(s)):
        if s[i] not in checked:
            return False
    return True
for _ in range(int(input())):
    s = input()
    if(base_three(s)):
        print("YES")
    else:
        print("NO")