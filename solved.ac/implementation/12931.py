n = int(input())
arr = list(map(int, input().split()))

cnt = 0

while any(arr):
  temp = [i for i in arr]
  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      temp[i] = arr[i] // 2
    else:
      arr[i] -= 1
      cnt += 1

      break
  else:
    arr = temp
    cnt += 1

print(cnt)

# import sys; input = sys.stdin.readline

# n = int(input())
# first = [0] * n 
# second = list(map(int, input().split()))

# visited = [False] * n 


# def dfs(index):
#   if visited[index]:
#     return 


#   for i in range(len(first)):
#     if first[i] == second[index]:

#   dfs(index + 1)