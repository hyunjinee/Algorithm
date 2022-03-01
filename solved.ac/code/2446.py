n = int(input())
for bin,star in zip(range(n-1), range(n*2-1 , 1, -2))  :
  print(' ' * bin + '*' * star)

for bin,start in zip (range(n-1, -1, -1), range(1, n* 2, 2)):
  # print(bin,start)
  print(' ' * bin + '*' * start)

# print(list(zip(range(n-1), range(n*2, 1, -2))))