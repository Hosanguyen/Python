
# tinh tong phan thuc
def tong_phan_thuc(n):
    if(n%2==0):
        i = 2
    else:
        i = 1
    sum = 0
    while(i<=n):
        sum += 1/i
        i+=2
    return sum
for i in range(int(input())):
    n = int(input())
    print('{0:.6f}'.format(tong_phan_thuc(n)))
    