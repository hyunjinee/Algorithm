from bisect import bisect_left

while True:
    try:
        n = int(input())
        array = list(map(int, input().split()))

        dp = [array[0]]

        for i in range(1, n):
            if array[i] > dp[-1]:
                dp.append(array[i])
            else:
                dp[bisect_left(dp, array[i])] = array[i]
        print(len(dp))
    except EOFError:
        break

# import sys
# input = sys.stdin.readline
# while True:
#     n = input()
#     if not n:
#         break
#     n = int(n)
#     array = list(map(int, input().split()))
#     dp = [0 for _ in range(n)]
#     dp[0] = array[0]
#     length = 1
#     for x in array[1:]:
#         start = 0
#         end = length - 1
#         index = 0
#         while start <= end:
#             mid = (start + end) // 2
            
#             if dp[mid] < x:
#                 start = mid + 1
#                 index = max(index, mid+1)
            
#             else:
#                 end = mid - 1
                
#         length = max(index+1, length)
#         dp[index] = x

#     print(length)