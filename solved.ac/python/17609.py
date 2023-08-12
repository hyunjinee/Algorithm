def isP_Palindrome(s):
    i, j = 0, len(s)
    while i < j:
        if s[i] != s[j-1]:
            return s[i+1:j] == s[i+1:j][::-1] or s[i:j-1] == s[i:j-1][::-1]
        i += 1
        j -= 1
    return True

n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s == s[::-1]:
        print(0)
        continue
    if isP_Palindrome(s):
        print(1)
    else:
        print(2)

# # 팰린드롬. , 유사회문
# # 회문인지, 또는 한 문자를 삭제하면 회문이 되는 유사 회문인지
# # 아니면 회문이나 유사회문도 아닌 일반 문자열인지 판단해야한다.
# # 회문 0 
# # 유사회문 1
# # 나머지 2

# import sys
# input = sys.stdin.readline
# t =int(input())

# def isPalindrome(s):
#   if s == s[::-1]:
#     print(0)
#     return 

#   for i in range(len(s)):
#     _s = s[:i] + s[i+1:]
#     if _s == _s[::-1]:
#       print(1)
#       return
  
#   print(2)
#   return
  

  

# for _ in range(t):
#   s = input().rstrip()
#   isPalindrome(s)
