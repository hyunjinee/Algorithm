n = int(input())
s = [input() for _ in range(n)]
s.sort(key=len)
ans = 0 
for i in range(n):
  current = s[i]
  head = False
  for j in range(i+1, n):
    if s[j].find(current) == 0:
      head = True
      break
  if not head:
    ans += 1
print(ans)
#
#  N=int(input())
# L=[]
# for i in range(N):
#     word=input()
#     L.append(word)

# L.sort(key=len)
# ans=0
# for i in range(N):
#     nowWord=L[i]
#     isHead=False
#     for j in range(i+1,N):
#         try:
#             if L[j].index(nowWord)==0:
#                 isHead=True
#                 break
#         except:
#             continue
#     if not isHead:
#         #print(nowWord)
#         ans+=1
# print(ans)
# import sys
# input = sys.stdin.readline
# n = int(input())
# # n개의 단어가 주어졌을 때 접두사 X 집합인 부분집합의 최대크기를 구하세용
# ans = 1

# s = [input().rstrip() for _ in range(n)]
# s.sort()



# test = []
# for i in range(n):
#   test.append(s[i])
#   for j in range(n):
#     if i == j: continue
#     # 테스트에있는 원소들과 비쇼해서, s[j]를 넣을 수 있는지 확인해야한다.
#     for t in test:
#       if s[j].find(t) != 0 and t.find(s[j]) != 0:

#     # for t in test:
#     #   if s[j].find(t) != 0 and t.find(s[j]) != 0:
#     #     continue
#     #   else: break
    
#   print(test)
#   test = []
#   # for j in range(n):
#   #   if i == j:
#   #     continue
#   #   if s[i].find(s[j]) != 0 and s[j].find(s[i]) != 0:
#   #     test.append(s[j])
#   # print(test)
#   # test = []


# # print(s)
# # for i in range(n):
# #   for j in range(n):
# #     if i == j :
# #       continue
# #     else:
# #       print(s[j].find(s[i]) )
# #       if s[j].find(s[i]) == 0:


# # temp = 0
# # for i in range(n):
# #   temp = 0
# #   for j in range(n):
# #     if i == j:
# #       continue
# #     if s[j].find(s[i]) != -1:
# #       temp += 1
# #   ans = max(ans, len(s) - temp)
# #   print(ans)
# # print(ans)