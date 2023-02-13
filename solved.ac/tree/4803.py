from sys import stdin
from collections import deque
input = stdin.readline

def find_tree(x):

    flag = True
    q=deque()
    q.append(x)

    while q:
        now = q.popleft()
        if visited[now]:
            flag = False
        visited[now] = True
        for next in tree[now]:
            if not visited[next]:
                q.append(next)

    return flag

count = 0

while True:
    count +=1
    n,m = map(int,input().split())
    if n==0 and m == 0: break

    tree = [ [] for _ in range(n+1)]
    visited = [False]*(n+1)

    for i in range(m):
        a,b=map(int,input().split())
        if a==b: continue
        tree[a].append(b)
        tree[b].append(a)

    result = 0

    for i in range(1,n+1):
        if visited[i]:
            continue
        if find_tree(i):
            result += 1

    if result == 0:
        print("Case {}: No trees.".format(count))
    elif result == 1:
        print("Case {}: There is one tree.".format(count))
    else:
        print("Case {}: A forest of {} trees.".format(count,result))