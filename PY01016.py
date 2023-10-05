def decode(s):
    for i in range(0, len(s), 2):
        c = s[i]
        x = int(s[i+1])
        for j in range(x):
            print(c, end = '')
    print()
for _ in range(int(input())):
    s = input()
    decode(s)