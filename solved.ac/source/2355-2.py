a, b = map(int, input().split())
n_max = max(a, b)
n_min = min(a, b)


amax = n_min*(n_min-1)//2
bmax = n_max*(n_max+1)//2

print(bmax-amax)