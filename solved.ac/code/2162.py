import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def check_twoline(l1,l2):
    if ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) <= 0 and\
        ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) <= 0:
        if ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) == 0 and\
            ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) == 0:
            if max(l1[0][0], l1[1][0]) >= min(l2[0][0], l2[1][0]) and \
                    max(l2[0][0], l2[1][0]) >= min(l1[0][0], l1[1][0]) and \
                    max(l1[0][1], l1[1][1]) >= min(l2[0][1], l2[1][1]) and \
                    max(l2[0][1], l2[1][1]) >= min(l1[0][1], l1[1][1]):
                return True
        else:
            return True
    return False

n = int(input())
temp, parent = [], [i for i in range(n)]
line = []
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    temp.append([[x1,y1],[x2,y2]])
    for j in range(i):
        if check_twoline(temp[i],temp[j]):
            line.append([i,j])

for a,b in line:
    union_parent(a,b)

result = defaultdict(int)
for i in range(n):
    result[parent[i]]+=1
print(len(result.keys()))
print(max(result.values()))