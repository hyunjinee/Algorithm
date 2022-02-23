N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
words = list(set(words))
sort_word =[]
for j in words:
    sort_word.append((len(j),j))

sort_word.sort() #sort() 는 앞의조건일치시 뒤를 정렬한다.
for len,voca in sort_word:
    print(voca)

