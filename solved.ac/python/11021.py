N = int(input())

for i in range(N):
    a,b = map(int, input().split())
    print("Case #%s: %s"%(i+1, a+b))