import sys
from collections import defaultdict

T = int(sys.stdin.readline())

a = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
listB = list(map(int, sys.stdin.readline().split()))

dictA = defaultdict(int)
ans = 0
for i in range(a):
    for j in range(i, a):
        dictA[sum(listA[i:j+1])] += 1
for i in range(b):
    for j in range(i, b):
        ans += dictA[T - sum(listB[i:j+1])]

print(ans)


# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# t = int(input())
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# dictA = defaultdict(int)
# print(dictA)
# ans =0 

# for i in range(n):
#   for j in range(i, a):
#     dictA[sum(a[i:j+1])] +=1 