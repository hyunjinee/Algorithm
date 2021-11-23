s = input()
li = []
for i in range(len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            li.append(t)
print(min(li))

# word = list(map(ord, input()))

# min_index = word.index(min(word))
# temp = min(word)
# word.pop(2)


# min_index2 = word.index(min(word))

# if min_index2 - 1 >= min_index:
#     # 오른쪽에 있으면 ?
#     min_index2 += 1

# word.insert(2, temp)


# word = (
#     word[0 : min_index + 1][::-1]
#     + word[min_index + 1 : min_index2 + 1][::-1]
#     + word[min_index2 + 1 :][::-1]
# )
# print("".join(map(chr, word)))
# # word = list(input())

# # for i in range(len(word)):

# #     word[i] = ord(word[i])

# # # print(word)

# # # print(word.index(min(word)))

# # l_index = word.index(min(word))

# # print(l_index)
# # r_index = word[l_index + 1 :].index(min(word[l_index + 1 :])) + l_index + 1


# # word = (
# #     word[0 : l_index + 1][::-1]
# #     + word[l_index + 1 : r_index + 1][::-1]
# #     + word[r_index + 1 :][::-1]
# # )

# # for i in range(len(word)):
# #     word[i] = chr(word[i])

# # print("".join(word))


# # # print(word)
# # # word.insert(l_index + 1, "/")
# # # word.insert(r_index + 2, "/")

# # # print(word)
# # # print(l_index, r_index)

# # # for i in range(len(word)):
# # #     word[i] = ord(word[i])


# # # print(word)


# # # 사전순으로 어떻게 ?
