# 대칭 차집합

alen,blen = map(int, input().split())



a = set(map(int, input().split()))
b = set(map(int, input().split()))


print(len(a-b) + len(b- a))
# if alen > blen:
#     for i in range(alen):
#         if a[i] in b:
#             del a[i]
#             del b[b.index(a[i])]
# else:
#     for i in range(blen):
#         if b[i] in a:
#             del b[i]
#             del a[a.index(b[i])]

# ans = a + b
# print(len(ans))
# ans = []
# for i in range(alen):

#     if a[i] not in b:
#         ans.append(a[i])
#     else: 
#         del b[b.index(a[i])]

# for i in range(len(b)):
#     if b[i] not in a:
#         ans.append(b[i])

# print(len(ans))


# 개 뻘짓 했다.


