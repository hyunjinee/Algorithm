
k = int(input())
def recursive(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  if n % 2:
    return 1 - recursive(n-1)
  else:
    return recursive(n//2)

print(recursive(k-1))


# k = int(input())

# x = '0'
# cnt = 0
# while True:
#   temp = x
#   x = x.replace('0', '2')
#   x = x.replace('1', '0')
#   x = x.replace('2', '1')
#   x = temp + x

#   if len(x) > k:
#     break

# print(x[k-1])



# while True:
#   temp = x
#   x = x.split()
#   for i in range(len(x)):
#     if x[i] == '0':
#       x[i] == '1'
#     else:
#       x[i] == '0'
#   print(x, "/")
#   x = ''.join(x)

#   x = temp + x
#   print(x)
#   if len(x) > k :
#     break

# print(x)