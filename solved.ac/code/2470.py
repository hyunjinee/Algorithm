# input 입력 받기
n = int(input())
solution = list(map(int, input().split(' ')))

# 정렬하기
solution.sort()

# 이중포인터 설정
left = 0
right = n-1
import sys
answer = sys.maxsize # 기준값
final = [] # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
	
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        right -= 1

print(final[0], final[1])

# import sys
# input = sys.stdin.readline

# n = int(input())
# liquids = list(map(int, input().split()))
# liquids.sort()

# head = 0 
# tail = len(liquids) - 1

# ans = sys.maxsize
# keep = []
# while head < tail:
#   if  abs (liquids[head] + liquids[tail] )  < ans:
#     ans = abs (liquids[head] + liquids[tail])
#     keep = [liquids[head], liquids[tail]]
#   if liquids[head] + liquids[tail] > 0:
#     tail -= 1
#   elif liquids[head] + liquids[tail] < 0:
#     head += 1
  
# keep.sort()

# print(*keep)