from math import *
import sys;input=sys.stdin.readline

def init(node, start, end):
  if start == end:
    tree_min[node] = arr[start]
    return tree_min[node]
  mid = (start+end) // 2
  tree_min[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
  return tree_min[node]

n, m = [int(x) for x in input().split()]
h = int(ceil(log2(n)))
t_size = 1 << (h+1)
arr =[]
tree_min = [0] * t_size
for _ in range(n):
  arr.append(int(input()))
