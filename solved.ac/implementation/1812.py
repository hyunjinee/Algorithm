N = int(input())
l = []
a = 0

for i in range(N):
    l.append(int(input()))
    a += (l[-1] if i%2==0 else -l[-1])
a //= 2
print(a)
j = a

for i in range(N-1):
    j = l[i]-j
    print(j)

# n = int(input())
# s = []
# sum = 0
# for i in range(n):
#     a = int(input())
#     s.append(a)
#     sum += a
# sum //= 2
# for i in range(n):
#     num = 0
#     for j in range(1, n, 2):
#         num += s[(i + j) % n]
#     print(sum - num)

# import sys

# input =sys.stdin.readline

# candies = [0 for _ in range(int(input()) + 1)]
# temp = [0] * len(candies)

# for i in range(3):
#   t = int(input())
#   temp[i+1] = t
# print(temp)

# s = sum(temp)

# a = int(sum(temp) / 2)

# print(a, 'hi')




# print(candies)