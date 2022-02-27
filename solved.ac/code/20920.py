import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
  a = input().strip()
  if len(a) < m:
    continue
  if d.get(a):
    d[a][0] += 1
  else:
    d[a] = [1, len(a), a]
temp = list(d.values())
temp.sort(key=lambda x: (-x[0] , -x[1], x[2]))
for t in temp:
  print(t[2])
# print(temp)
# print (d.values())
# print(list(d.items()))
# print(d.items())

# words = [ ]
# for _ in range(n):
#   a = input().rstrip()
#   if len(a) >= m:
#     words.append(a)
# word_cnt = defaultdict(int)
# for i in range(len(words)):
#   if word_cnt[words[i]] == 0:
#     temp = words.count(words[i])
#     word_cnt[words[i]] += temp
# ans = sorted ( word_cnt.items(), key=lambda x: (-x[1], len(x[0]), x[0] ))
# for a in ans:
#   print(a[0])
# ans = sorted (word_cnt.items(), key=lambda x:( -x[0], -len(x[1]), x[1] ))
# temp = []
# for a, b in word_cnt.items():
#   temp.append((b, a))
# temp.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))
# for t in temp:
#   print(t[1])

# temp = []

# for a,b in word_cnt.items():
#   temp.append((b,a))
# temp.sort(reverse=True)

# temp.sort(key=lambda x: ( -len(x[1]), x[1] ))
# temp.sort(key=lambda x: x[0], reverse=True)



# for _,b  in temp:
#   print(b)
