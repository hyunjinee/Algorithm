import collections
import sys
from functools import cache

sys.setrecursionlimit(10000000)

N = int(sys.stdin.readline())
a = collections.defaultdict(list)
for _ in range(N-1):
    x, y = map(int,sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)

depth, parent = [-1]*(N+1), [-1]*(N+1)
depth[1], parent[1] = 0, 1

def dfs(x,d):
    for y in a[x]:
        if depth[y] == -1:
            depth[y] = d
            parent[y] = x
            dfs(y,d+1)
dfs(1,0)

@cache
def lca(x,y):
    if depth[x] > depth[y]: x, y = y, x
    while depth[x] < depth[y]: y = parent[y]
    while x != y: x, y = parent[x], parent[y]
    return x


for _ in range(int(sys.stdin.readline())):
    x, y = map(int,sys.stdin.readline().split())
    sys.stdout.write(str(lca(x,y))+"\n")