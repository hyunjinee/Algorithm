l = int(input())
s = list(map(int,input().split()))
n = int(input())
s.sort()
# s 1 7 14 10

start = 0 

while s[start]< n:
  start+=1
if s[start] == n:
  result = 0
elif start == 0 :
  result = n * (s[start] - n ) -1
else :
  result = (n - s[start-1]) * (s[start] - n) - 1
print(result)
# from itertools import combinations

# ss = list(combinations(s,2))
# 집합 s 와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수
# for sss in ss:

#   pass

# print(ss)

# a=0
# while info[a]<n:
#     a+=1

# if info[a]==n:
#     result=0
# elif a==0:
#     result=n*(info[a]-n)-1
# else:
#     result=(n-info[a-1])*(info[a]-n)-1
# print(result)

# a=input()
# x=sorted(map(int,input().split()))
# m=int(input())
# if m in x:
#     print(0)
# else:
#     p,q=0 if min(x)>m else max([i for i in x if i<m]),min([i for i in x if i>m])
#     print((m-p)*(q-m)-1)

# import sys;input=sys.stdin.readline
# l = int(input())
# arr = list(map(int,input().split()))
# n = int(input())


# n 을 포함하는 좋은 구간의 개수를 구하여라
# L = int(input())
# nums = list(map(int, input().split()))
# target = int(input()) # == n

# nums.append(0)
# nums.sort()

# A = 0
# for i in range(len(nums)-1) :
#     if nums[i] == target or nums[i+1] == target:
#         A = 0
#         break
#     elif nums[i] < target and target < nums[i+1]:
#         A = (target - nums[i]) * (nums[i+1] - target) - 1
#         break

# print(A)
