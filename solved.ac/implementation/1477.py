import sys; input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

start, end = 1, l - 1
result = 0
while start <= end:
  count = 0
  mid = (start + end) // 2
  for i in range(1, len(arr)):
    if arr[i]-arr[i-1] > mid:
      count += (arr[i]-arr[i-1]-1)//mid
  if count > m:
    start = mid + 1

  else:
    end = mid - 1
    result = mid

print(result)
# # 현재 휴게소 개수, 
# # 더 지으려고하는 휴게소의 개수
# # 고속도로의 길이. L
# # 이미 휴게소 있는곳에 휴게소 세울수 없고 고속도로의 끝에도 휴게소 세울 수 없음

# lst = list(map(int, input().split()))
# lst.sort()

# lst.insert(0, 1)
# lst.insert(len(lst), l)


# visited = [0] * (l + 1)

# for i in lst:
#   visited[i] = 1

# while m > 0:
#   temp = []

#   for i in range(len(lst) - 1):
#     temp.append(lst[i + 1] - lst[i])

#   max_value = max(temp)
#   max_index = temp.index(max_value)

#   lst.insert(max_index + 1, (lst[max_index + 1] + lst[max_index] ) // 2)
  
#   print(lst)
  
#   m -= 1

# temp_length = []

# for i in range(len(lst) - 1):
#   temp_length.append(lst[i + 1] - lst[i])


# print(temp_length)
# print(min(temp_length))
