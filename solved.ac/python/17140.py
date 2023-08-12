

from collections import Counter
import sys
input = sys.stdin.readline
r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(3)]

def rc():
  max_len = 0
  row_count= len(a)
  for i in range(row_count):
    temp = [e for e in a[i] if e != 0]
    temp = Counter(temp).most_common()
    temp.sort(key = lambda x: (x[1], x[0]))
    a[i] = []
    for x,y in temp:
      a[i].append(x)
      a[i].append(y)
    len_temp = len(temp)
    if max_len < len_temp * 2 : max_len = len_temp * 2
  for j in range(row_count):
    for k in range(max_len - len(a[j])):
      a[j].append(0)
    a[j] = a[j][: 100]
for i in range(101):
  try:
    if a[r-1][c-1] == k:
      print(i)
      break
  except:
    pass
  if len(a) < len(a[0]):
    a = list(zip(*a))
    rc()
    a = list(zip(*a))
  else:
    rc()
else:
  print(-1)






# import sys
# from collections import defaultdict
# input =sys.stdin.readline
# r,c,k = input().split()
# a = [list(map(int,input().split())) for _ in range(3)]
# isR = True
# while True:
#   if isR:
#     for i in range(3):
#       temp = defaultdict(int)
#       for j in range(len(a[i])):
#         if a[i][j] not in temp.keys():
#           temp[a[i][j]] = a[i].count(a[i][j])
#       print(temp)
#       b = sorted (temp.items(), key = lambda x: (x[1], x[0]))
#       print(b)
#   break



# seconds = 0
# while seconds <= 10:
#   c_cal = False
#   if r <= len(a) and c <= len(a[0]) and a[r-1][c-1] == k : break
#   if len(a) < len(a[0]):
#     c_cal = True
#     a = list(zip(*a))
#   new_a = []
#   max_len = 0
#   for row in a:
#     counter = Counter(row)
#     if counter[0] : del counter[0]
#     temp = list(map(list, counter.items()))
#     temp.sort(key = lambda x: (x[1], x[0]))
#     new_a .append(list(sum(temp, []) ))



  
#   new_a = []
#   max_len = 0
#   for row in a:
#     counter = Counter(row)
#     if counter[0]: del counter[0]
#     temp = list(map(list, counter.items()))
#     temp.sort(key = lambda x: (x[1],x[0]))
#     new_a.append(list(sum(temp, []))[:100])
#     max_len = max(max_len, len(new_a[-1]))
    
#   for i in range(len(new_a)):
#     if len(new_a[i]) < max_len:
#       new_a[i] += [0] * (max_len - len(new_a[i]))
  
#   a = new_a

#   if c_cal: a = list(zip(*a))
#   seconds += 1
# print(seconds if seconds <= 100 else -1)
# for t in range(101):
#   if r-1 < len(A) and c-1 < len(A[0]) and A[r-1][c-1] == k : print(t); break
#   if len(A) >= len(A[0]): A = op(A)
  # else: A = list(zip(*op(list(zip))))

# def rc():
#   len_a = len(a)
#   for j in range(len_a):
#     temp = [i for i in a[j] if i != 0]
#     temp = Counter(a).most_common()
#     print(temp)



# for i in range(10):
#   try:
#     if a[r-1][c-1] == k:
#       print(i)
#       break
#   except:
#     pass
#   rc()
# def rc():
#   max_len = 0
#   len_s = len(s)
#   for j in range(len(s)):
#     a = [i for i in s[j] if i != 0]
#     a = Counter(a).most_common()
#     a.sort(key = lambda x: (x[1], x[0]))
#     s[j]= []
#     for fi,se in a:
#       s[j].append(fi)
#       s[j].append
# (se)
#     len_a = len(a)
#     if max_len < len_a * 2: max_len = len_a * 2
#   for j in range(len_s):
#     for k in range(max_len -len(s[j])):
#       s[j].append(0)
#     s[j] = s[j][:100]
# for i in range(101):
#   try:
#     if s[r-1][c-1] == k:
#       print(i)
#       break
#   except:
#     pass

#   if len(s) < len(s[0]):
#     s = list(zip(*s))
#     s = list(zip(*s))
#   else:
#     rc()
# else:
#   print(-1)

