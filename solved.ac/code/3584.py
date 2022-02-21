import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    p_list=[0 for _ in range(N+1)] 
    for _ in range(N-1):
        p,c=map(int,sys.stdin.readline().split())
        p_list[c]=p                    
    a,b=map(int,sys.stdin.readline().split())
    a_parent=[a]
    b_parent=[b]                               
    while p_list[a]:
        a_parent.append(p_list[a])
        a=p_list[a]
    while p_list[b]:
        b_parent.append(p_list[b])
        b=p_list[b]
    a_level=len(a_parent)-1
    b_level=len(b_parent)-1
    while a_parent[a_level]==b_parent[b_level]:  
        a_level-=1
        b_level-=1
    print(b_parent[b_level+1])

# import sys
# input = sys.stdin.readline
# t = int(input())
# def find(x):
#   if x == parent[x]:
#     return x
#   else:
#     parent[x] = find(parent[x])
#     return parent[x]
# for _ in range(t):
#   n = int(input())
#   tree = [[] for _ in range(n + 1)]
#   parent = [i for i in range(n + 1)]
#   for __ in range(n - 1):
#     a,b = map(int, input().split())
#     parent[b] = a
#   # print(parent, "here")
#   x, y = map(int, input().split())
#   top = -1
#   for i in range(1, n+1):
#     if i == parent[i]:
#       top = i
#       break
#   # print(top, "top")
#   xParent = [x]
#   while top != x:
#     temp = parent[x]
#     xParent.append(temp)
#     x = temp
#   while top != y:
#     temp = parent[y]
#     if temp in xParent:
#       print(temp)
#       break
#     y = temp










#   # print(xParent, "xParent")
#   # print(xParent)
#   # ytemp = y
#   # while True:
#   #   if x == parent[x]:
#   #     xParent.append(x)
#   #     break
#   #   else:
#   #     temp = find(parent[x])
#   #     xParent.append(temp)
#   #     parent[x] = temp

#   # while True:
#   #   if y == parent[y] and y in xParent :
#   #     print(y, "gogogogoog")
#   #     break
#   #   else:
#   #     parent[y] = find(parent[y])

     
     