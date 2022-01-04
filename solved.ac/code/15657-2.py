
n, m = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()
solve = []

def Dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return

    for i in range(n):
        if depth == 0 or solve[depth - 1] <= my_list[i]:
            solve.append(my_list[i])
            Dfs(depth + 1)
            solve.pop()

Dfs(0)