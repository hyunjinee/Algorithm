n, m = map(int, input().split())
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x: 
        return x
    p = find(parent[x])
    parent[x] = p
    return p
def union(x, y):
    x = find (x)
    y = find (y)
    if x >= y:
        parent[y] = x
    else:
        parent[x] = y

trueList = list(map(int, input().split()))
for i in range(trueList[0]):
    union(trueList[1], trueList[i+1])

party = [ ]

for _ in range(m):
    party.append(list(map(int, input().split())))
    party_num = party[-1][0]
    for cur in range(party_num - 1):
        union(party[-1][cur+1], party[-1][cur+2])
ans = 0

for i in party:
    for cur in range(i[0]):
        if (len(trueList)) > 1 and find(i[cur+1]) == find(trueList[1]):
            ans+=1
            break
print(m - ans)


# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# a = input().rstrip()

    
# # a is number of people and b is people's number
# # b is 1 ~ N
# # M line party people and number
# # find the maximum lies

# parties = [list(map(int, input().split())) for _ in range(M)]

# if a != '0':
#     a,b = a.split()
#     b = list(map(int, b))
# else :
#     print(len(parties))
#     exit()
# # 지민이를 0 번이라고 했을 때, 지민이와 connected component
# # 를 만들어 버리면?? 연결되어있으니까 
# ans = 0

# for party in parties:
#     for people in b:
#         if people in party[1:]:
#             continue
#         else: 
#             print(party, people)
#             ans += 1


# print(ans)