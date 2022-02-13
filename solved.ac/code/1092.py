
from sys import stdin
N = int(stdin.readline())
crane = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
boxs = list(map(int, stdin.readline().split()))
crane.sort(reverse=True)
boxs.sort(reverse=True)
if boxs[0]>crane[0]:
    print(-1)
    exit()
ans=0
while boxs:
	i=0 # box
	cnt=0
	j=0 # crane

	while j<N and i<len(boxs):
		if boxs[i]<=crane[j]:
			cnt+=1
			j+=1
			del boxs[i]
		else:
			i+=1
		if cnt==N:
			break
	if cnt<N:
		N=cnt
	ans+=1
print(ans)

# n = int(input())
# crane = list(map(int, input().split()))
# m = int(input())
# box = list(map(int, input().split()))

# # ⚡ 내림차순 정렬
# crane.sort(reverse = True)
# box.sort(reverse = True)

# time = 0 # 시간
# checked = [0 for _ in range(m)] # 박스를 옮겼는지 여부
# count = 0 # 옮긴 박스의 개수 

# positions = [0] * n

# if max(box) > max(crane):
#     print(-1)
# else:
#     while count < len(box):
#         for i in range(n): # 크레인에 대하여
#             while positions[i] < len(box):
#             # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
#                 if not checked[positions[i]] and crane[i] >= box[positions[i]]:
#                     checked[positions[i]] = True
#                     positions[i] += 1
#                     count += 1
#                     break
#                 positions[i] += 1
#         time += 1
#     print(time)   

# # import sys
# # input = sys.stdin.readline

# # n = int(input())
# # w = list(map(int, input().split()))
# # m = int(input())
# # boxes = list(map(int ,input().split()))
# # boxes.sort(reverse=True)
# # w.sort(reverse=True)
# # cnt = 0 
# # # print(boxes)
# # while len(boxes) != 0:
# #   for i in range(len(w)):
# #     for j in range(len(boxes)):
# #       if w[i] >= boxes[j]:
# #         boxes.pop(j)
# #         break
  
# #   cnt += 1

# #   if len(boxes) == 0:
# #     print(cnt)
# #     exit()


# # print(cnt)