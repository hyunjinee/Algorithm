s = input()

p = 0
ans = 0
for i in range(len(s)):
    if s[i] == '(':
        p += 1
    else:
        p -= 1
        ans += p if s[i - 1] == '(' else 1


# bar_razor = list(input())
# answer = 0
# st = []

# for i in range(len(bar_razor)):
#     if bar_razor[i] == '(':
#         st.append('(')

#     else:
#         if bar_razor[i-1] == '(': 
#             st.pop()
#             answer += len(st)

#         else:
#             st.pop() 
#             answer += 1 

# print(answer)




# bar_razor = list(input())
# answer = 0
# stack = []

# for i in range(len(bar_razor)):
#     if bar_razor[i] == '(': #스택 쌓기
#         stack.append('(')
        
#     else:
#         if bar_razor[i-1] == '(': #()라면 (를 pop하고 현재 스택에 들어있는 ( 수만큼 값을 더해준다.
#             stack.pop()
#             answer += len(stack)
            
#         else:
#             stack.pop() 
#             answer += 1 #끄트머리 막대기 부분을 더해준다

# print(answer)


# # print(ans)
# # # import sys
# # # input = sys.stdin.readline
# # # stack = []
# # # res = 0
# # # strings = input().rstrip()
# # # for i in range(len(strings)):
# # #   if stack and strings[i-1] == '(' and strings[i] == ')':
# # #     stack.pop()
# # #     res += len(stack)
# # #   elif stack and stack[-1] == '(' and strings[i] == ')':
# # #     stack.pop()
# # #     res += 1
# # #   else: 
# # #     stack.append(strings[i])

# # # print