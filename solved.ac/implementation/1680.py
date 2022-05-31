from collections import deque

for _ in range(int(input())):
    W, n = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]

    queue = deque(li)
    distance = 0 # 거리 0 초기화
    while queue:
        current = 0
        while queue:
            x, w = queue.popleft()

            if w + current == W:
                distance += x * 2
                break
            elif w + current < W:
                if not queue:
                    distance += x * 2
                current += w
            else:
                distance += x * 2
                queue.appendleft((x, w))
                break

    print(distance)


# # T = int(sys.stdin.readline())
# # for _ in range(T):
# #     W, N = map(int, sys.stdin.readline().split())
# #     arr = [
# #            list(map(int, sys.stdin.readline().split()))
# #            for _ in range(N)
# #     ]
# #     dist_sum = 0
# #     # execute
# #     while arr:
# #         pos, dist, weight = 0, 0, 0
# #         for i in range(len(arr)):
# #             weight += arr[i][1]
# #             if weight == W:
# #                 dist = arr[i][0]
# #                 pos = i
# #                 break
# #             elif weight > W:
# #                 dist = arr[i][0]
# #                 pos = i - 1
# #                 break
# #             elif i == len(arr) - 1:
# #                 dist = arr[i][0]
# #                 pos = i
# #         dist_sum += dist * 2
# #         if len(arr) - 1 > pos:
# #             arr = arr[pos + 1:]
# #         else:
# #             break

# #     print(dist_sum)

# # # import sys
# # # input = sys.stdin.readline

# # # test_case = int(input())

# # # for _ in range(test_case):
# # #     weight, N = map(int,input().split())
    
# # #     dist = 0
# # #     plus_dist = 0
# # #     now_w = 0

# # #     over = False

# # #     for i in range(1, N + 1):
# # #         x, w = map(int,input().split())

# # #         plus_dist = x
# # #         now_w += w
# # #         if i == N:
# # #             if now_w > weight:
# # #                 dist += plus_dist * 4

# # #             else:
# # #                 dist += plus_dist * 2
        
# # #         else:    
# # #             if now_w > weight:
# # #                 now_w = w
# # #                 dist += plus_dist * 2

# # #                 if w == weight:
# # #                     dist += plus_dist * 2
# # #                     now_w = 0
            
# # #             elif now_w == weight:
# # #                 dist += plus_dist * 2
# # #                 now_w = 0
        
# # #     print(dist)

# # # # t = int(input())


# # # # for _ in range(t):
# # # #     plan = []
# # # #     target_w, n = map(int, input().split())
# # # #     for _ in range(n):
# # # #         x_i, w_i = map(int, input().split())
# # # #         plan.append([x_i, w_i])

# # # #     w = 0
# # # #     now = 0
# # # #     ans = 0
# # # #     for d, ww in plan:
# # # #         # 일단 직진
# # # #         ans += d-now
# # # #         w += ww
# # # #         now = d

# # # #         # 용량 상황에 따라 해결
# # # #         if w == target_w:
# # # #             # 비우기
# # # #             ans += now
# # # #             now = 0
# # # #             w = 0
# # # #         elif w > target_w:
# # # #             # 비우기
# # # #             ans += now
# # # #             now = 0
# # # #             w = 0
# # # #             # 돌아오기
# # # #             now = d
# # # #             ans += d
# # # #             w += ww

# # # #     # 마지막 쓰레기
# # # #     ans += now
# # # #     print(ans)

# # # # # if __name__ == '__main__':
# # # # #     for _ in range(int(input())):
# # # # #         w, n = map(int, input().split())
# # # # #         testcase = []
# # # # #         for __ in range(n):
# # # # #             x_i, w_i = map(int, input().split())
# # # # #             testcase.append([x_i, w_i])

# # # # #         capacity = 0
# # # # #         distance = 0
# # # # #         previous_value = 0
# # # # #         for i in testcase:
# # # # #             # i[0]: 쓰레기장으로부터의 거리   i[1]: 쓰레기의 양
# # # # #             if capacity + i[1] < w:
# # # # #                 distance += i[0] - previous_value
# # # # #                 capacity += i[1]
# # # # #             elif capacity + i[1] == w:
# # # # #                 distance += (i[0] - previous_value) + i[0] * 2
# # # # #                 capacity = 0
# # # # #                 if testcase.index(i) == n - 1:
# # # # #                     distance -= i[0] * 2
# # # # #             elif capacity + i[1] > w:
# # # # #                 capacity = i[1]
# # # # #                 distance += (i[0] - previous_value) + i[0] * 2
# # # # #             previous_value = i[0]

# # # # #         # 모든 쓰레기를 수거하여 다시 쓰레기장으로 돌아갈 때
# # # # #         if testcase.index(i) == n - 1:
# # # # #             distance += i[0]

# # # # #         print(distance)

# # # # # # import sys
# # # # # # input =sys.stdin.readline


# # # # # # for _ in range(int(input())):
# # # # # #   ans = 0
# # # # # #   w,n  = map(int, input().split())
# # # # # #   trash = [list(map(int,input().split())) for _ in range(n)]

# # # # # #   # trash.sort(key=lambda x: (x[0], x[1]))
# # # # # #   temp = 0
# # # # # #   i = 0

# # # # # #   while i != len(trash):
# # # # # #     a,b = trash[0]
# # # # # #     if temp + b < w:
# # # # # #       temp += b
# # # # # #       i += 1

# # # # # #     elif temp + b == w:
# # # # # #       ans += a * 2
# # # # # #       temp = 0
# # # # # #       i += 1
# # # # # #     elif temp + b > w:
# # # # # #       b = b - (w - temp)
# # # # # #       temp += b
# # # # # #       ans += a * 2
# # # # # #       while b > 0:
# # # # # #         b = b - w 
# # # # # #         ans += a * 2
# # # # # #       temp = 0
# # # # # #       i = i + 1
        

# # # # # #   print(ans)