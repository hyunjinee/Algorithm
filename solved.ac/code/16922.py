S = set()
N = int(input())
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            l = N - (i+j+k)
            if i+j+k+l == N and l >-1:
                S.add(i + 5*j + 10*k + 50*l)
print(len(S))
# n = int(input().strip())

# lst = []

# for i in range(n + 1):
#     for j in range(n + 1 - i):
#         for k in range(n + 1 - i - j):
#             t = n - i - j - k
#             total = i * 1 + j * 5 + k * 10 + t * 50
#             lst.append(total)

# print(len(set(lst)))
# import sys
# input = sys.stdin.readline
# n = int(input())
# loma = [1, 5, 10,50]
# ans = []
# def dfs(start, cnt):
#   if cnt >= n:
#     if sum(start) not in ans:
#       ans.append(sum(start))
#     return 
#   for i in range(len(loma)):
#     start.append(loma[i])
#     dfs(start, cnt + 1)
#     start.pop()
# dfs ([], 0)
# print(len(ans) )
# loma = ["I", "V", "X","L"]

# combi = list(permutations(loma, n))
# print(combi)

# ans = []

# for c in combi :
#   if sum(c) not in ans:
#     ans.append(sum(c))
# print(ans)