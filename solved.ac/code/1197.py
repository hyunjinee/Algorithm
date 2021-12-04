import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(E)]

Vroot = [i for i in range(V + 1)]

edges.sort(key=lambda x: x[2])


def find(x):
    if Vroot[x] == x:
        return x
    Vroot[x] = find(Vroot[x])
    return Vroot[x]


answer = 0
for s, e, w in edges:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
print(answer)
