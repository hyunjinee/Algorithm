# n = int(input())
# lst = [int(input()) for _ in range(n)]
# lst.sort()
# ans = []
# for i in range(1, n+1):
#   temp = lst[-i : ]
#   ans.append(temp[0] * i )
# # 소팅 한다음에 1개의 로프, 2개의 로프, 3개의 로프 사용할 때 
# print(max(ans))

def solution():
  answer = 0
  arr.sort(reverse=True)
  for i in range(n):
    arr[i] = arr[i] * (i + 1)

  return max(arr)

n = int(input())

arr = []
for _ in range(n):
  arr.append(int(input()))

print(solution())
