n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
# n, m = map(int, input().split())

# visited = [False] * n
# out = []


# def solve(depth, n, m):
#     if depth == m:
#         print(' '.join(map(str, out)))
#         return

#     for i in range(len(visited)):
#         if not visited[i]:
#             visited[i] = True
#             out.append(i+1)
#             solve(depth+1, n, m)
#             visited[i] = False
#             out.pop()


# solve(0, n, m)
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# # 길이가 m 인 수열, 1~ n 까지 중복 없이 골라야함

# l = [i for i in range(1, n + 1)]

# # 어떻게 만들것인가 ?
# print(l)


# visited = [False for _ in range(n+1)]

# for i in range(m):

#     # dfs나 그런 재귀인건 맞는데 어떻게 할껀데 ??????
#     #
