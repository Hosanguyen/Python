for _ in range(int(input())):
    s = input()
    i = 0
    min = 0
    while(i != len(s)):
        if(s[i].isdigit()):
            j = i + 1
            while(j<len(s) and s[j].isdigit()):
                j += 1
            tmp = 0
            for k in range(i, j):
                tmp = tmp*10 + int(s[k])
            if tmp > min: min = tmp
            i = j
        else: i += 1
    print(min)