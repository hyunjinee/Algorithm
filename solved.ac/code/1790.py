n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9


while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit
if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])

# n, k = map(int, input().split())
# ans = 0
# digit = 1
# nine = 9

# while k > digit * nine:
#     k = k - (digit * nine)
#     ans += nine
#     digit += 1
#     nine = nine * 10

# ans = (ans + 1) + (k - 1)
# # print(ans, ">??")
# if ans > n:
#   print(-1)
# else: 
#   print(str(ans)[(k-1)%digit])

# # N, k = map(int,input().split())

# # digit = 1
# # pos = 0
# # all = 0

# # while True:
# #   if k - ( 9 *(10 ** (digit- 1)) ) <= 0:
# #     break
# #   k = k - ( 9 *(10 ** (digit- 1)))
# #   digit += 1
# #   all += digit * (9 ** (digit -1))

# # if digit == 1:
# #   print(k)
# #   exit()
# # l = -1
# # # print(k,digit)
# # if k % digit == 0:
# #   count = k // digit
# #   all += count * digit
# #   l = 0
# # else: 
# #   count = k // digit + 1
# #   all += count * digit
# #   l = k % digit
# # start = 10 ** (digit -1 )

# # end = start + count - 1
# # if all < k:
# #   print(-1)
# #   exit()
# # print(str(end)[l-1])
# # # print(end)