import sys
S=list(input())
T=list(input())
def dfs(t):
    if t==S:
        print(1)
        sys.exit()
    if len(t)==0:
        return 0
    if t[-1]=='A':
        dfs(t[:-1])
    if t[0]=='B':
        dfs(t[1:][::-1])
dfs(T)
print(0)

# import sys


# # 백 트래킹을 통해 완성된 문자열로 시작 문자열을 만들 수 있는지 확인
# def solution(c):
#     global flag

#     if len(c) == len(s):
#         if c == s:
#             flag = True

#         return

#     if c[0] == "B":
#         c.reverse()
#         c.pop()
#         solution(c) # 백 트래킹
#         c.append("B")
#         c.reverse()

#     if c[-1] == "A":
#         c.pop()
#         solution(c) # 백 트래킹
#         c.append("A")


# s = list(map(str, sys.stdin.readline().strip()))
# t = list(map(str, sys.stdin.readline().strip()))
# flag = False
# solution(t)

# if flag:
#     print(1)
# else:
#     print(0)