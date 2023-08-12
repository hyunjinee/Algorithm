from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    print(stack)
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)

# import sys;input=sys.stdin.readline
# n = int(input())
# a = list(map(int,input().split()))
# from collections import Counter
# c = Counter(a)
# most_common = c.most_common()[0][0]
# for i in range(n):
#   if a[i] == most_common:
#     print(-1, end=' ')
#     continue

#   for j in range(i+1, n):
#     if c[a[j]] > c[a[i]]:
#       print(a[j], end= ' ')
#       break


# print(most_common)
# print(c.most_common())
# print(dict(c))




# from collections import Counter

# arr_count = Counter(arr)
# result = [-1] * n
# stack = [0]
# for i in range(n):
#   print(stack)
#   while stack and arr_count[arr[stack[-1]]]  < arr_count[arr[i]]:
#     print(arr[stack[-1]], arr_count[arr[stack[-1]]])
#     result[stack.pop()] = arr[i]
#   stack.append(i)

# print(*result)
# for i in range(1, n):
#   while stack and 
# print(arr_count)
# from sys import stdin
# from collections import Counter

# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))

# ngf = [-1] * n
# c = Counter(a)
# s = [0]

# for i in range(n):
#     while s and c[a[s[-1]]] < c[a[i]]: ngf[s.pop()] = a[i]
#     s.append(i)

# print(*ngf)
