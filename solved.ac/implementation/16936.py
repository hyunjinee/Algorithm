n = int(input())
B = list(map(int, input().split()))
minB = min(B)
maxB = max(B)

def check(nx):
    if minB <= nx <= maxB and (nx in B) and (nx not in A):
        A.append(nx)
        return 1
    return 0

def dfs(x):
    if x % 3 == 0:
        if check(x // 3):
            return dfs(x // 3)
        if check(x * 2):
            return dfs(x * 2)
    else:
        if check(x * 2):
            return dfs(x * 2)

for x in B:
    A = [x]
    dfs(x)
    if len(B) == len(A):
        print(*A, end=' ')
        break