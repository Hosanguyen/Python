def tong(n):
    if(n<10):
        return
    
    tong(a+b)

n = int(input())
while(n>10):
    s = str(n)
    a = int(s[0:int(len(s)/2)])
    b = int(s[int(len(s)/2):len(s)])
    n = a + b
    print(n)