import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
h_sum = sum(h)

if h_sum % 3 != 0:
  print('No')
  exit()


turn = h_sum // 3 
for apple in h :
  turn -= (apple//2)
if turn > 0:
    print('No')
else:
    print('Yes')
# import sys
# input = sys.stdin.readline

# N = int(input())
# h = list(map(int,input().split()))

# two = 0
# one = 0
# for wood in h:
#     two += wood//2
#     one += wood%2
#     print(two, one)

# if not (two-one)%3 and two >= one:
#     print('YES')
# else:
#     print('NO')

# # n = int(input())
# # arr = list(map(int, input().split()))
# # total = sum(arr)
# # cnt = sum(x%2 for x in arr)
# # if total%3:
# #   print("NO")
# # elif cnt > total//3:
# #   print("NO")
# # else:
# #   print("YES")

