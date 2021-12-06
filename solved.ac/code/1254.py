s = input()
n = len(s)
for i in range(n):
    if s[i:] == s[i:][::-1]:
        print(n + i)
        break
# s = input()


# def is_palindrome(s):
#     reversed_str = list(reversed(s))
#     for i in range(len(reversed_str)):
#         if s[i] == reversed[i]:
#             continue
#         else:
#             return False
#     return True


# if is_palindrome(s):
#     print(len(s))
# else:
#     reversed_str = list(reversed(s))
#     for i in range(len(s) - 1, 0, -1):
#         if is_palindrome(reversed[:i]):
#             print(len(s) * 2 - i)
#         elif i == 1:
#             print(len(s) * 2)
