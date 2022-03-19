# https://hyunjinee.tistory.com/32
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
heights = list(map(int,input().split()))
costs = []
for i in range(n-1):
  costs.append(heights[i+1]-heights[i])
costs.sort(reverse=True)
print(sum(costs[k-1:]))