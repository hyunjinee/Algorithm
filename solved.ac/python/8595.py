n=int(input())
s=input()
numbers='1234567890'
tmps=''
for i in s:
    if i in numbers : tmps+=i
    else: tmps+=' '
print (sum( list(map(int, tmps.split()))))


# hidden number.
# 연속된 숫자는 한 히든 넘버이다.
# 두 히든 너버사이에는 글자가 적어도 한개 있다.
# 히든 넘버는 6자리를 넘지 않ㄴ느다. 

# length = int(input())

# _sum = 0

# s = input()
# temp = ''
# for i in range(length):
#     if s[i].isdigit():
#       temp += s[i]
#     else:
#       if temp == '':
#         continue


#       _sum += int(temp)
#       temp = ''

# print(_sum)
