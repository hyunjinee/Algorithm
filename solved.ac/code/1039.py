n, k = input().split()
m = len(n)
s = {n}
for _ in range(int(k)):
  if len(s) == 0:break
  ans = set()
  while s:
    nums = list(s.pop())
    for i in range(len(n)-1):
      for j in range(i+1, len(n)):
        temp = nums[:]
        temp[i], temp[j] = temp[j], temp[i]
        if temp[0]!='0': ans.add(''.join(temp))
  s = ans
if len(s) == 0: print(-1)
else: print(max(s))



# for _ in range(k):
#     if len(S)==0:break;
#     new = set()
#     while S:
#         nums = list(S.pop())
#         for i in range(N-1):
#             for j in range(i+1,N):
#                 n = nums[:]
#                 n[i],n[j] = n[j],n[i]
#                 if n[0]!='0': new.add(''.join(n))
#     S = new
# if len(S)==0:print(-1)
# else: print(max(S))

# n, k = map(int, input().split())
# answer = 0
# record = []

# def swap(num, k) :
#   global answer
#   global record

#   if k == 0:
#     answer = max(answer, int(num))
#   if (num, k ) in record:
#     return 
#   else:
#     record.append((num,k))

#   m = len(str(n))

#   for i in range(m):
#     for j in range(i+1, m):
#       if not (i == 0 and num[j] == '0'):
#         swap((num[:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]), k - 1)
# swap(str(n), k)

# print(-1 if answer == 0 else answer)
