n=int(input())
a=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    b=[a[1]]
    for j in range(1,9):
        b.append(a[j-1]+a[j+1])
    b.append(a[8])
    a = b
sum_ = 0
for k in a:
    sum_ += k
print(sum_%1000000000)