n =int(input())

pattern = input().split("*")

print(pattern)
for _ in range(n):
  inputString = input()
  if inputString[:len(pattern[0])] == pattern[0] and inputString[-len(pattern[1]):] == pattern[1] and len("".join(pattern)) <=len(inputString) :
    print("DA")
  else:
    print("NE")

# n=int(input())
# pattern=str(input())
# front=''
# back=''
# idx=0
# for i in range(len(pattern)):
#     if pattern[i]=='*':
#         idx=i+1
#         break
#     front+=pattern[i]
# for i in range(idx, len(pattern)):
#     back+=pattern[i]
# for i in range(n):
#     file=str(input())
#     if len(file)<len(front)+len(back):
#         print('NE')
#     elif file[:len(front)]==front and file[-len(back):]==back:
#         print('DA')
#     else:
#         print('NE')

# import sys
# input = sys.stdin.readline
# test_case = int(input())
# pattern = input().rstrip()


# for _ in range(test_case):

#   word = input().rstrip()

#   i ,j = 0, 0

#   while True:
#     if j > len(word) : break

#     try:

#       if pattern[i] == word[j]:
#         i += 1
#         j += 1
#       elif pattern[i] == '*'  and pattern[i+1] == word[j] :
#         i += 1
#         j += 1
#       elif pattern[i] == '*'  and pattern[i] != word[j]:
#         j += 1
#       elif pattern[i] != word[j]:
#         continue
#     except IndexError:
#       print("NE")
#       break
    
#   print('YES' if i == len(pattern) else 'NO')