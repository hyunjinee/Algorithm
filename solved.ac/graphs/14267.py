import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
tmp = list(map(int, input().split()))
relation = [[] for _ in range(n+1)]
superior = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for i in range(n):
    if tmp[i] == -1:
        continue
    relation[tmp[i]].append(i+1)
    superior[i+1] = tmp[i]
for _ in range(m):
    r, v = map(int, input().split())
    answer[r] += v
def delivery(cur):
    answer[cur] += answer[superior[cur]]
    if relation[cur]:
        for nxt in relation[cur]:
            delivery(nxt)
delivery(1)
print(*answer[1:])
