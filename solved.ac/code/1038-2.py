def _1038(n, sum, arr, res):
    if n == -1:
        res.append(sum)
        return
    _1038(n-1, sum, arr, res)
    _1038(n-1, (sum * 10) + n, arr,  res)


arr = [0,1,2,3,4,5,6,7,8,9]
res = []
N = int(input())
if N >= 1023:
    print('-1')
    exit()

_1038(9, 0, arr, res)
res.sort()
print(res[N + 1])



# sys.setrecursionlimit(10**6)
# global enumerate
# num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# input = sys.stdin.readline
#
# digit = 2
# temp = [0 for i in range(2)]
#
# global ans
#
# ans = []
# i = 0
# def dfs(arr,digit,depth):
#     pass
#
# n = int (input())
# if n >= 1023:
#     print(-1)
# else:
#     for digit in range(1, 11):
#         arr = [0 for _ in range(digit)]
#         for i in range(10-digit+1):
#             arr[0] = num[i]
#             dfs (arr, digit, 1)
#
#         if len(ans) >= n + 1 :
#             break
#     ans.sort()
#     print(ans[n])