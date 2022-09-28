n = int(input())
word = input()
cnt = 0

for i in range(n):
  if i == n // 2:
    break
  if word[i] != word[-(i + 1)]:
    cnt += 1

print(cnt)