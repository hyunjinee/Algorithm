import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().strip().split())
arr = [0 for _ in range(1000001)]

for i in range(N):
    ice, x = map(int, input().strip().split())
    arr[x] = ice

q = deque()
maxIce = 0
tempIce = 0
for i in range(0, 1000001):
    q.append(arr[i])
    tempIce += arr[i]
    if (2*K+1) < len(q):
        tempIce -= q.popleft()
    maxIce = max(maxIce, tempIce)

print(maxIce)
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# arr = [0] * 1000001

# for _ in range(N):
#     g, x = map(int, input().split())
#     arr[x] = g

# step = K * 2 + 1
# temp = sum(arr[:step])
# ans = temp

# for i in range(step, 1000001) :
#     temp += arr[i] - arr[i - step]
#     ans = max(ans, temp)

# print(ans)

# import sys
# from collections import deque
# input = sys.stdin.readline


# N, K = map(int, input().split())
# buckets = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
# q = deque()
# cur = 0
# total = 0
# mx = 0

# for ice, pos in buckets:
#     cur = max(pos - K, 0)

#     total += ice
#     q.append((pos, ice))

#     while q[0][0] < cur - K:
#         total -= q.popleft()[1]

#     if mx < total:
#         mx = total
# print(mx)
# # import sys
# # input = sys.stdin.readline
# # N,K = map(int, input().split())
# # whitebear_list = [0] * 1000001
# # end = 0

# # for _ in range(N):
# #     g, x = map(int, input().split())
# #     whitebear_list[x] = g
# #     end = max(end, x)

# # step = 2*K+1
# # window = sum(whitebear_list[:step])
# # answer = window


# # for i in range(step, end+1):
# #     window += whitebear_list[i] - whitebear_list[i-step]
# #     answer = max(answer, window)
# # print(answer)

# # import sys
# # from collections import deque

# # n,k=map(int, sys.stdin.readline().split())
# # ice=[0]*(10**6+1)
# # maxk=0
# # q=deque()
# # for i in range(n):
# #     g,x=map(int, sys.stdin.readline().split())
# #     ice[x]=g
# #     if maxk<x: maxk=x
# # max=0
# # temp=0
# # for i in range(0,maxk+1):
# #     if len(q)==(2*k+1):
# #         temp-=q.popleft()
# #     q.append(ice[i])
# #     temp+=ice[i]
# #     if max<temp:
# #         max=temp
    
# # print(max)

# # # import sys
# # # from collections import defaultdict
# # # input = sys.stdin.readline

# # # # left, right : 양동이가 위치한 가장 좌측과 우측
# # # # start, end : 투 포인터
# # # # curr : 현재 얼음의 양

# # # n, k = map(int,input().rsplit())
# # # ice = defaultdict(int)
# # # min_l, max_l, answer = sys.maxsize, 0, -1

# # # for _ in range(n):
# # #     g, x = map(int,input().rsplit())
# # #     ice[x] = g
# # #     max_l = max(max_l, x)
# # #     min_l = min(min_l, x)

# # # end, curr = min_l, 0
# # # for start in range(min_l, max_l + 1):
# # #     while end < max_l + 1 and end - start <= k * 2:
# # #         if ice[end] == 0:
# # #             end += 1
# # #             continue
# # #         curr += ice[end]
# # #         end += 1
# # #     answer = max(answer, curr)
# # #     curr -= ice[start]
    

# # # print(answer)