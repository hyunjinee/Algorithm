#java로 변환
def tojava(text):
    #첫번째 or 마지막 문자가 _일때 __가 있을때
    if text[0] == "_" or text[-1] == "_" or "__" in text:
        return "Error!"

    ans=""
    flag=False    

    for i in text:
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90:
            return "Error!"

        if i == "_":
            flag = True
            continue

        if flag == True:
            ans += i.upper()
            flag=False
            continue

        ans+=i

    return ans
        
#c++로 변환
def toc(text):
    #첫 문자가 대문자 일때
    if ord(text[0])>=65 and ord(text[0])<=90:
        return "Error!"

    ans=""

    for i in text:
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90:
            ans+="_"+i.lower()
        else:
            ans+=i

    return ans


text = input()

if "_" in text:
    print(tojava(text))
else:
    print(toc(text))

# s = input()
# if s.find('_') > -1 :
#   for i in range(len(s)):
#     if s[i] == s[i].upper():
#       print('Error!')
#       exit()


# if s.find('_') > -1 : 
#   temp = ''
#   flag = False
#   for i in range(len(s)):
#     if s[i] == '_':
#       flag = True
#       continue
#     else:
#       if flag:
#         temp += s[i].upper()
#         flag = False
#       else:
#         temp += s[i]
# else:

#   temp = ''
#   for i in range(len(s)):
#     if s[i] == s[i].upper():
#       temp += '_' + s[i].lower()
#     else :temp += s[i]

# print(temp)