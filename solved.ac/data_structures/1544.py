result = 0
arr =[]
for _ in range(int(input())):
  word = input()
  if word not in arr:
    result +=1
    for _ in range(len(word)) :
      word = word[1:] + word[0]
      arr.append(word)
print(result)
# import sys;input=sys.stdin.readline
# n = int(input())

# words = {}

# for _ in range(n):
#   word = input().rstrip()
#   print(word)
#   print(word.split())
#   # word = "".join(word.split().sort())
#   # print(word)