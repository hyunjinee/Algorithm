l = int(input())
word = input()

table = [0 for _ in range(l+1)]

def kmp(word,length):
  pt = 1
  pp = 0
  while pt != length:
    if word[pt] == word[pp]:
      pt, pp = pt + 1, pp + 1
      table[pt] = pp
    elif pp == 0 :
      pt += 1

    else:
      pp = table[pp]

kmp(word, l)

print(l - table[l])