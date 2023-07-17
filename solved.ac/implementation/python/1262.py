import sys
input = sys.stdin.readline
def diamond(N, r, c):
    r = r % (2*N-1)
    c = c % (2*N-1)
    mid = abs(N-1-r)
    index = abs(N-1-c) + mid
    if index > N-1:
        return '.'
    else:
        return chr((index % 26)+97)

N, r1, c1, r2, c2 = map(int, input().split())

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(diamond(N, i, j), end='')
    if i != r2:
        print()

# n,r1,c1,r2,c2 = map(int, input().split())


# def make_diamond(x, diamond):
#   if x == 1:
#     diamond[n-1][n-1] = 'a'
#     return 

#   for i in range(0, len(diamond)):
#     for j in range(0, len(diamond)):
#       if abs((n-1) - i) + abs((n-1) - j) == x - 1:
#         diamond[i][j] = chr(ord('a') + (x - 1))
#   make_diamond(x-1, diamond)
  
#   return diamond

# ans = make_diamond(n, [['.'] * (2 * n - 1) for _ in range(2 * n - 1)])

# for i in range(r1, r2+1):
#   for j in range(c1, c2+1):
#     print(ans[i % (2 * n - 1)][j % (2 * n - 1)], end='')
#   print()


# print(ans)
# for bo in board:
#   print(bo)


# def print_arr():
#     global arr
#     for r in range(1, 2 * N):
#         for c in range(1, 2 * N):
#             print(arr[r][c], end='')
#         print()


# N, R1, C1, R2, C2 = [int(x) for x in input().split(' ')]


# for r in range(R1, R2 + 1):
#     for c in range(C1, C2 + 1):
#         dr = (r % (2 * N - 1)) + 1
#         dc = (c % (2 * N - 1)) + 1
#         if 1 <= dr <= N and 1 <= dc <= N - dr:
#             print('.', end='')
#         elif N + 1 <= dr <= 2 * N - 1 and 1 <= dc <= dr - N:
#             print('.', end='')
#         elif 1 <= dr <= N and N + dr <= dc <= 2 * N - 1:
#             print('.', end='')
#         elif N + 1 <= dr <= 2 * N - 1 and 2 * N - dr + N <= dc <= 2 * N - 1:
#             print('.', end='')
#         else:

#             if 1 <= dr <= N:
#                 tr = dr
#             else:
#                 tr = 2 * N - dr
#             tc = abs(N - dc)
#             print(chr(ord('a') + (N - (tr - tc))%26), end='')
#     print()





