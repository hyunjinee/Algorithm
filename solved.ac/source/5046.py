N,B,H,W = map(int, input().split())
pay = []
tusuk = []
for i in range(H):
    p = int(input())
    pay.append(p)
    numbers = list(map(int ,input().split()))
    tusuk.append(numbers)
#print(tusuk)
paylist = []
for j in range(H):
    if pay[j]*N <=B:
        for k in range(W):
            if tusuk[j][k] >= N:
                 paylist.append(pay[j]*N)
    else:
        pass
if paylist:

    print(min(paylist))
else:
    print("stay home")                


