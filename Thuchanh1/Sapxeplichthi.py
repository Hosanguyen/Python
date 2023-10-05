class thi:
    def __init__(self, macathi, date, time, maphong, mon, manhom, solg):
        self.macathi = macathi
        self.date = date
        self.time = time
        self.maphong = maphong
        self.mon = mon
        self.manhom = manhom
        self.solg = solg
    
    def getData(self):
        print(self.date, self.time, self.maphong, self.mon, self.manhom, self.solg)

def cmp(lthi):
    return lthi.time + lthi.macathi

with open('MONTHI.in') as rf:
    vb = rf.read()
monthi = vb.split('\n')
with open('CATHI.in') as rf:
    vb = rf.read()
cathi = vb.split('\n')
with open('LICHTHI.in') as rf:
    vb = rf.read()
lichthi = vb.split('\n')



List = []
n = int(monthi[0])
j = 2
k = 1
l = 1
for i in range(n):
    macathi = ""; date = ""; time = ""; maphong = ""; mon = ""; manhom = ""; solg = ""
    mon = monthi[j]
    date = cathi[k]
    time = cathi[k+1]
    maphong = cathi[k+2]
    tmp = lichthi[l].split()
    macathi = tmp[0]
    manhom = tmp[2]
    solg = tmp[3]
    addthi = thi(macathi, date, time, maphong, mon, manhom, solg)
    List.append(addthi)
    j+=3
    k+=3
    l+=1
List.sort(key = cmp)
for x in List:
    x.getData()

