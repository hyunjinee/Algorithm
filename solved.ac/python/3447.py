import sys
text = sys.stdin.read()
while "BUG" in text:
    text = text.replace("BUG", "")
print(text)

# import sys 
# import re
# code=sys.stdin.readlines()


# print(code )
# for i in code:     
#     while True:
#         result=re.sub('BUG','',i)         
#         if 'BUG' in result: i= result
#         else: 
#             print(result,end="") 
#             break

# # # bug ? 

# import sys
# input =sys.stdin.readline

# cnt = 0 

# while cnt < 101:
#   cnt += 1


#   s = input()


#   s  = s.replace("BUG", "")

#   print(s)



# # while True:

# #   s = input().rstrip()
# #   if (len(s)) == 0 :

# #     break

# #   s = s.replace('BUG', '')

# #   print(s)