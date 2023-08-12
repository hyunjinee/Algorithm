m, n  = map(int ,input().split())
nums = [str(i) for i in range(m, n+1)]
s = {
  '1' : 'one',
  '2' : 'two',
  '3' : 'three',
  '4' : 'four',
  '5' : 'five',
  '6' : 'six',
  '7' : 'seven',
  '8' : 'eight',
  '9' : 'nine',
  '0' : 'zero',
} 
ans = [ ]
for i in nums:
  # print(i ,'this is i')
  temp = ''
  for j in range(len(i)):
    # print(i[j] ,'this is j')
    # print(s[nums[i][j]], 'check please')
    temp += s[i[j]]
    temp += ' '
  temp = temp[:-1]
  ans.append((temp, i))

ans.sort()

# print(*ans)

for i in range(len(ans)):
  if i % 10 == 0  and i > 1:
    print()
  print(ans[i][1], end=' ')