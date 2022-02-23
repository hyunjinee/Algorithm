# N, M = map(int, input().split())

# Alist = list(input().split())
# Blist = list(input().split())

import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
nmlist = list(map(int, input().split())) + list(map(int, input().split()))
print(' '.join(map(str, sorted(nmlist))))


# Clist = Alist + Blist
# for C in sorted(Clist):
#     print(C, end=" ")


# def add_1(n):
#       return n + 1

# target = [1, 2, 3, 4, 5]

# result = map(add_1, target)

# print(list(result)) 