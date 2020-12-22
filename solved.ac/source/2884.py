H , M = map(int, input().split())
if H==0 and M <=44:
    print(23, 60-(45-M) )
# (H*60+M)
elif H!=0 and M<=44:
    print(H-1, 60-(45-M))
elif H!=0 and M>44:
    print(H, M-45 )
elif H==0 and M>44:
    print(0, M-45)