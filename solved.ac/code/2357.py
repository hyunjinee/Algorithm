import sys
from math import *


input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
h = int (ceil(log2(n))) 
t_size = 1 << (h + 1)
arr = []
tree_min = [0] * t_size
tree_max = [0] * t_size

for _ in range(n):
  arr.append(int(input()))

def initMin(node, start, end):
  if start == end:
    tree_min [node] = arr[start]
    return tree_min[node]
  mid = (start + end) // 2
  tree_min[node] = min(initMin(node * 2 , start, mid) , initMin(node * 2 + 1 , mid + 1 , end))
  return tree_min[node]

def initMax(node, start, end) :
  if start == end: 
    tree_max[node] = arr[start]
    return tree_max[node]
  mid = (start + end) // 2
  tree_max[node] = max(initMax(node * 2 , start, mid) , initMax(node * 2 + 1 , mid + 1 , end))

initMin(1, 0 , n-1)
initMax(1, 0 , n-1)
for _ in range(m):
  a, b = [int(x) for x in input().split()]

# print(h, "?")
# print(t_size)

# def initMin(node, start ,end ):
#   if start == end:
#     tree_min[node] = arr[start]






# import heapq
# n, m = map(int,input().split())
# heap = []

# for _ in range(n):

#   heap.append(int(input()))

# heapq.heapify(heap)
# print(heap)
# for _ in range(m):
#   a, b = map(int, input().split())


