import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

for i in range(1, int(input())+1):
    n = int(input())
    p = [i for i in range(n)]
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        if find(p, a) != find(p, b):
            union(p, a, b)
    print('Scenario '+str(i)+':')
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if find(p, a) != find(p, b): print(0)
        else: print(1)
    print()