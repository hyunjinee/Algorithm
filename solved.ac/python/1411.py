import sys
input = sys.stdin.readline
n = int(input())
word = [input().rstrip() for _ in range(n)]
cnt =0 
for i in range(0, n-1):
  for j in range(i+1, n):
    s1 = list(word[i])
    s2 = list(word[j])
    flag = True
    if len(s1) == len(s2):
      visit1 = [0] * 26
      visit2 = [0] * 26

      for k in range(len(s1)):
        idx1 = ord(s1[k]) - ord('a')
        idx2 = ord(s2[k]) - ord('a')
        if visit1[idx1] == 0 and visit2[idx2] == 0:
          visit1[idx1] = s2[k]
          visit2[idx2] = s1[k]
        elif visit1[idx1] != s2[k]:
          flag = False
          break
    if flag:
      cnt += 1

print(cnt)