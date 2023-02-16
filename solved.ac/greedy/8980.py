import sys
input = sys.stdin.readline

n, capacity = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
ans = 0
send = []
for _ in range(m):
  a, b, amount = map(int, input().split())
  send.append([a,b,amount])

send.sort(key = lambda x: (x [1] , x[0]))

for start, destination, boxes in send:
  maxbox = boxes
  for i in range(start, destination):
    maxbox = min(maxbox, capacity - box[i])
  for i in range(start, destination):
    box[i] += maxbox
  ans += maxbox

print(ans)
# n, space = map(int, input().split())
# m = int(input())
# box = [0] * (n + 1)
# send = []
# answer = 0
# # 1. 도착하는 마을 마다 가장 빨리 도착하는 순서부터 최대로 담는다 - 틀림
# # 2. [받는 마을, 보내는 마을] 순으로 정렬한다.
# for i in range(m):
#     a, b, amount = map(int, input().split())
#     send.append([a, b, amount])
# send.sort(key=lambda x: (x[1], x[0]))

# for start, destination, boxes in send:
#     maxbox = boxes
#     # start부터 dest까지 얼만큼 박스를 보낼 수 있는지 검사
#     for i in range(start, destination):
#         maxbox = min(maxbox, space - box[i])
#     # 박스를 담는 동시에 answer 또한 +, 어차피 담은 박스는 반드시 배달된다.
#     for i in range(start, destination):
#         box[i] += maxbox
#     answer += maxbox
# print(answer)


# import sys

# if __name__ == "__main__":
#     n, c = map(int, sys.stdin.readline().split())
#     m = int(sys.stdin.readline())
#     box = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


#     box.sort(key=lambda x:x[1])  # 도착 시간이 빠른 순서로 정렬

#     answer = 0  # 최대 박스 수
#     remain = [c] * (n + 1)  # 각 위치에 남은 공간

#     for i in range(m):
#         temp = c  # c개를 옮길 수 있다고 가정
#         for j in range(box[i][0], box[i][1]):
#             temp = min(temp, remain[j])
#         temp = min(temp, box[i][2])
#         for j in range(box[i][0], box[i][1]):
#             remain[j] -= temp
#         answer += temp

#     print(answer)

# # import sys
# # input = sys.stdin.readline

# # n, c = map(int, input().split())
# # m = int(input())

# # boxes = [list(map(int, input().split())) for _ in range(m)]
# # boxes.sort(key=lambda x:(x[1])) # 마을 도착 시간이 빠른 것 순으로 정렬

# # count = 0
# # remains = [c]*(n+1) # 마을 당 수용가능한 박스 수

# # for i in range(m):
# #     temp = c # c개를 옮길 수 있다고 가정
# #     for j in range(boxes[i][0], boxes[i][1]):
# #         temp = min(temp, remains[j])
# #     temp = min(temp, boxes[i][2])
# #     for k in range(boxes[i][0], boxes[i][1]):
# #         remains[k] -= temp
# #     count += temp

# # print(count)






# # # from sys import stdin

# # # N, C =  map(int, stdin.readline().split())
# # # M = int(stdin.readline())
# # # infos = []
# # # for _ in range(M):
# # #     s, r, box = map(int, stdin.readline().split())
# # #     infos.append((s, r, box))
# # # infos.sort(key=lambda x :  x[1])

# # # capa = [C]*N
# # # total = 0
# # # for s, r, box in infos:
# # #     _min = C
# # #     for i in range(s, r):
# # #         if _min > min(capa[i], box) :
# # #             _min = min(capa[i], box)
# # #     for i in range(s, r):
# # #         capa[i] -= _min
# # #     total += _min
# # # print(total)
# # # # import sys
# # # # input = sys.stdin.readline

# # # # n, c = map(int, input().split()) # 마을의 수와 트럭의 용량
# # # # m = int(input())

# # # # delivery = []

# # # # for _ in range(m):
# # # #   delivery.append(list(map(int, input().split())))

# # # # delivery.sort(key = lambda x: (x[0], x[1], -x[2]))

# # # # print (delivery)


# # # # capacity = 0

# # # # for i in range(1, n + 1):


  
# # # #   pass
