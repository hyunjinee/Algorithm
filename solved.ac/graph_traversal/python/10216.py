from sys import stdin, stdout

def uff(a):
    if parent[a] == a:
        return a
    parent[a] = uff(parent[a])
    return parent[a]

def ufu(a, b):
    pa = uff(a)
    pb = uff(b)
    if pa != pb:
        parent[pa] = pb

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    parent = [i for i in range(n)]
    tower = []
    for i in range(n):
        x,y,r1 = map(int, stdin.readline().split())
        for j in range(i):
            a,b,r2 = tower[j]
            if (x-a)**2 + (y-b)**2 <= (r1+r2)**2:
                ufu(i,j)
        tower.append((x,y,r1))
            
    ans = set()
    for i in range(n):
        ans.add(uff(i))
    stdout.write(f"{len(ans)}\n")

# import sys, math
# input = sys.stdin.readline
# # union find 풀이
# def get_parent(x):
#   if parent[x] == x:
#     return x
#   parent[x] = get_parent(parent[x])
#   return parent[x]

# def find_group(x1, x2):
#   parent1 = get_parent(x1)
#   parent2 = get_parent(x2)

#   if parent1 > parent2:
#     parent[parent1] = parent2
#   else:
#     parent[parent2] = parent1

  



# for _ in range(int(input())):
#   n = int(input())
#   array = [list(map(int, input().split())) for _ in range(n)]
#   parent = [i for i in range(n)]

#   for i in range(n):
#     x1, y1, r1 = array[i]
#     for j in range(i + 1, n):
#       x2, y2, r2 = array[j]

#       if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1 + r2:
#         find_group(i, j)
  
#   count_group = set()

#   for i in range(n):
#     x = get_parent(i)

#     if x not in count_group:
#       count_group.add(x)

#   print(len(count_group))

# # dfs 풀이

# # def distance(a, b):
# #     return (a[0]-b[0])**2+(a[1]-b[1])**2

# # def dfs(cur):
# #     for j in range(n):
# #         if distance(location[cur], location[j])>(location[cur][2]+location[j][2])**2 or cur==j or visited[j]:
# #             continue
# #         visited[j]=True
# #         dfs(j)
# # t=int(input())
# # for _ in range(t):
# #     n=int(input())
# #     answer=0
# #     location=[]
# #     visited=[False for _ in range(n)]
# #     for _ in range(n):
# #         location.append(list(map(int, input().split())))
# #     for i in range(n):
# #         if not visited[i]:
# #             dfs(i)
# #             answer+=1
# #     print(answer)