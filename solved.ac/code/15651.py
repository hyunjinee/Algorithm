N, M = map(int, input().split())

# 1 부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러번 고르기 가능
s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()


dfs()
