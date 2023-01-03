n=int(input())
mp, mf, ms, mv=map(int, input().split())
foods=[]
for _ in range(n):
    foods.append(list(map(int, input().split())))
min_cost=987654321
ans=[]
def dfs(food, number, index):
    global min_cost, ans
    if mp <= food[0] and mf <= food[1] and ms<= food[2] and mv <= food[3] and food[4] < min_cost:
        min_cost=food[4]
        ans=number.copy()
    for idx, fd in enumerate(foods):
        if idx<=index:
            continue
        for i in range(5):
            food[i] += fd[i]
        number.append(idx+1)
        dfs(food, number, idx)
        for i in range(5):
            food[i]-=fd[i]
        number.pop()
dfs([0, 0, 0, 0, 0], [], -1)
if ans:
    print(min_cost)
    print(*ans)
else:
    print(-1)
# n=int(input())
# mp, mf, ms, mv=map(int, input().split())
# foods=[]
# for _ in range(n):
#     foods.append(list(map(int, input().split())))
# min_cost=987654321
# ans=[]
# visited = [False] * n
# def dfs(food, number, index):
#     global min_cost, ans, visited
#     if visited[index] == True:
#       return

#     visited[index] = True
#     if mp <= food[0] and mf <= food[1] and ms<= food[2] and mv <= food[3] and food[4] < min_cost:
#         min_cost=food[4]
#         ans=number.copy()
#     for idx, fd in enumerate(foods):
#         for i in range(5):
#             food[i] += fd[i]
#         number.append(idx+1)
#         dfs(food, number, idx)
#         for i in range(5):
#             food[i]-=fd[i]
#         number.pop()
#     visited[index] = False

# dfs([0, 0, 0, 0, 0], [], 0)
# if ans:
#     print(min_cost)
#     print(*ans)
# else:
#     print(-1)

# # import sys; input =sys.stdin.readline

# # def pass_or_not(v, used_idx):
# #   global mn

# #   for i in range(4):
# #     if req[i] > v[i]:
# #       return False
# #   mn = v[4]
# #   mn_idx.clear()
# #   mn_idx.extend(used_idx)
# #   return


# # def dfs(l,v, used_idx):
# #   global mn
# #   if v[4] >= mn:
# #     return 

# #   if pass_or_not(v,used_idx):
# #     return

# #   if l == n:
# #     return 

# #   else:

# #     used_idx.append(l + 1)
# #     for i in range(5):
# #       v[i] += data[l][i]
# #     dfs(l + 1, v, used_idx)

# #     used_idx.pop()

# #     for i in range(5):
# #       v[i] -= data[l][i]

# #     dfs(l + 1, v, used_idx)



# # n = int(input())
# # req = list(map(int, input().split()))
# # data = [list(map(int, input().split())) for _ in range(n)]
# # mn = 9876543210
# # mn_idx = [] 

# # res = dfs(0, [0,0,0,0,0], [])

# # # inf = 9876543210

# # # def calculate ( do, picked, pick_sum) :
# # #   global chosen, tot_prc
# # #   if pick_sum[4] >= tot_prc:
# # #     return 
# # #   for i in range(4):
# # #     if req_nut[i] > pick_sum[i]:
# # #       break
# # #   else:
# # #     chosen = picked.copy()
# # #     tot_prc = pick_sum[4]
# # #   if do == n:
# # #     return 
# # #   picked.append(do + 1)
# # #   for i in range(5):
# # #     pick_sum[i] += nuts[do][i]

# # #   calculate(do + 1 ,picked, pick_sum)

# # #   picked.pop()

# # #   for i in range(5):
# # #      pick_sum[i] -= nuts[do][i]
# # #   calculate(do + 1, picked, pick_sum)

# # #   return 




# # # n = int(input())
# # # req_nut = tuple(map(int, input().split()))
# # # nuts = tuple(tuple(map(int, input().split())) for _ in range(n))
# # # chosen = []

# # # tot_prc = inf


# # # calculate(0, [], [0, 0, 0, 0, 0])

# # # if tot_prc == inf :
# # #   print(-1)
# # # else:
# # #   print(tot_prc)
# # #   print(*chosen)