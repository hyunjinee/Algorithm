t = int(input())
for _ in range(t):
  ans = ''
  flag= False
  lst = list(map(int,input()))
  for i in range(len(lst) - 1, -1, -1):
    if lst[i] <= lst[i-1]:
      continue
    else:
      lst[i:] = sorted(lst[i:])
      for idx, j in enumerate(lst[i:]):
        if j > lst[i-1]:
          lst[i-1], lst[idx+i] = lst[idx+i], lst[i-1]
          flag =True

          for a in range(len(lst)):
            ans += str(lst[a])
          print(ans)
          break
      if flag: 
        break
  if not flag: 
    print("BIGGEST")





      # for idx, num in enumerate(lst[i:]):
      #   if lst[i-1] < num:

      # break

  # print(lst)

  # a = defaultdict(int)
  # a = []
  # n = input().rstrip()



  # for i in range(len(n)):

  #   a.append(int(n[i]))

  # # 모두 넣어주고 다음 숫자를 찾아야함. 

  # 123 -> 132




  # print(a)