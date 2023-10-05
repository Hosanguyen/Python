n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(len(a)):
   j = i+1
   while(j<len(a) and a[j]==a[i]):
      a.remove(a[j])
#print(a)

n = len(a)
x =[]

for i in range(k+1):
   x += [0]

def display():
    for i in range(1, len(x)):
        print(a[x[i]-1], end = ' ')
    print()

def Try(i):
   for j in range(x[i-1]+1, n-k+i+1):
      x[i] = j
      if(i==k):
         display()
      else:
         Try(i+1)

Try(1)  