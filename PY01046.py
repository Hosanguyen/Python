def trade(a, b):
    print(a + " -> " + b)
def thap_Ha_Noi(n, a, b, c):
    if(n==1):
        trade(a, c)
    else:
        thap_Ha_Noi(n-1, a, c, b)
        thap_Ha_Noi(1, a, b, c)
        thap_Ha_Noi(n-1, b, a, c)
n = int(input())
thap_Ha_Noi(n, 'A', 'B', 'C')
