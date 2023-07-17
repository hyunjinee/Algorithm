import sys; input = sys.stdin.readline
word_count = int(input())
base_word = list( input().rstrip() )
words = [input().rstrip() for _ in range(word_count - 1)]
ans = 0

for word in words:
  compare_word = base_word[:]
  word_lst = list(word)
  for _ in range(len(word)):
    a = word_lst.pop(0)
    if a in compare_word:
      compare_word.remove(a)

    else:
      word_lst.append(a)
    
  A = len(compare_word)
  B = len(word_lst)

  if (A == 0 and B == 0) or (A == 1 and B == 0) or (A == 0 and B == 1) or (A == 1 and B == 1):
    ans += 1
  
print(ans)
