import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)

# import sys
# input = sys.stdin.readline

# def makeP(n):
#   if n == 1:
#     return 'IOI'
#   else: 
#     temp = 'IOI'
#     for i in range(n):
#       temp += 'OI'
#     return temp

# n = int(input())
# m = int(input())
# s = input().rstrip()

# if len(s) < 3:
#   print(0)
#   exit()

# p = makeP(n)
# cnt = 0
# for i in range(m):
#   if s.find(p) == -1:
#     print(cnt)
#     exit()
#   else: 
#     idx = s.find(p)
#     cnt +=1
#     s = s[idx+len(p) - 1:]
# print(cnt)