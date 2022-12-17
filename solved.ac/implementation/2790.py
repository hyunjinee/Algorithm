import sys
n = int(sys.stdin.readline())
alist=[]
for i in range(n):
    alist.append(int(sys.stdin.readline().replace("\n","")))
alist =sorted(alist, reverse=True)
amax, count=0,0
for i in range(len(alist)):
    amax = alist[i]+i+1 if amax<alist[i]+i+1 else amax

for i in alist:
    count = count+1 if i+len(alist)>=amax else count