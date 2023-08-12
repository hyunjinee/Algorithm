# 대소문자로 된  단어가 주어짐. 
# 이 단어에서 가장 많이 사용된 알파벳은 뭘까용




word = input().upper()

count = {}

for alphabet in word:
    if alphabet in count:
        count[alphabet] += 1
    else:
        count[alphabet] = 1


# print(count.values())
max_value = max(count.values())
count_max_value = 0
ans = ''
for e, i in count.items():
    if i == max_value:
      count_max_value += 1
      ans = e
    
if count_max_value != 1: 
  print("?")
else :
  print(ans)
