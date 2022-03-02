t = int(input())
def dfs(level, exp, n):
    if level==n:
        a = exp.replace(' ', '')
        if eval(a) == 0:
            print(exp)
        return
    dfs(level+1, exp+' '+str(level+1), n)
    dfs(level+1, exp+'+'+str(level+1), n)
    dfs(level+1, exp+'-'+str(level+1), n)
for _ in range(t):
    n = int(input())
    dfs(1, '1', n)
    print()