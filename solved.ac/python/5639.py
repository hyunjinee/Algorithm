# 이진 검색 트리는 다음 같은 세가지 조건을 만족하는 이진 트리이다.
"""
노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽 오른족 서브트리도 이진 검색 트리이다.
"""

# 이진 검색 트리를 전위 순회한 결과가 주어질 때 이 트리를 후위 순회한 결과를 구하세용.


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def post_order(start,end) :
  if start > end :
    return 
  root = pre_order[start]
  idx = start + 1
  while idx <= end:
    if pre_order[idx] > root: 
      break

    idx += 1
  post_order(start + 1 , idx - 1)
  post_order(idx, end)
  print(root)
  

pre_order = [ ]

while 1: 
  try:
    pre_order.append(int(input()))
  except:
    break

post_order(0, len(pre_order ) - 1)
# def solve ( start, end ) :
#   if start > end: 
#     return 

#   div = end + 1



# tree = []
# count = 0

# while count <= 10000:
#   try:
#     temp = int(input())
#   except:
#     break

#   tree.append(temp)
#   count += 1
