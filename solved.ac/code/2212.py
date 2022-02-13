N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

distance = []
for i in range(len(sensor)-1):
  distance.append(sensor[i+1] - sensor[i])

distance = sorted(distance, reverse=True)
print(sum(distance[K-1:]))
# import sys
# input = sys.stdin.readline

# N = int(input())
# K = int(input())
# pts = list((map(int,input().split())))
# pts.sort()
# diff = []
# l = len(pts)
# for n in range(l-1):
#     diff.append(pts[n+1]-pts[n])
# diff.sort()
# print(sum(diff[:len(diff)-(K-1)]))


# # import sys
# # input = sys.stdin.readline

# # # 도로공사가 유비쿼트스화를 하가ㅣ위해 n개의 센서를 설치. k개의 집중국을 세울
# # # 수신 가능 영역을 조절. 연결된 구간으로 나타난다. 
# # n = int(input()) # sensor
# # k = int(input()) # house
# # sensor = list(map(int, input().split())) 

# # if k >= n :
# #   print(0)

# # else :
# #   sensor.sort()
  
# #   gap = []

# #   for  i in range(1, n):
# #     gap.append(( sensor[i] -  sensor[i-1], i) )
# #   gap.sort()

# #   standard = [0]
# #   result = 0

# #   for i in range(k-1):
# #     standard.append(gap.pop()[1])
# #   standard.append(0)

# #   result = 0
# #   for i in range(k):
# #     result += sensor[standard[i+1] - 1] - sensor[standard[i]]
# #   print(result)