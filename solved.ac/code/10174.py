for _ in range(int(input())):
    s = input().lower()
    print("Yes" if s == s[::-1] else "No")

# #  모든 라인에 대하여 팰린드롬인지 아닌지를 구분
# import sys
# input = sys.stdin.readline

# n = int(input())


# def isPalindrome(s):
#     s = s.lower()
#     # print(s, s[::-1])

#     return s == s[::-1]


# for i in range(n):
#     if isPalindrome(input().rstrip()):
#         print('Yes')
#     else:
#         print("No")
#         # isPalindrome(input().strip())
