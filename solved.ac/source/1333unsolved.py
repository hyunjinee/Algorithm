N,L,D = map(int, input().split())
lst = []
for k in range(1, N+1):
    for x in range(1,L*(2*N-1)//D):
        if k*L <= D*x <k*L +5 :
            lst.append(D*x)


if lst :
    print(min(lst))
else:
    print(L*(2*N-1))