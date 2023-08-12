from collections import Counter


N = int(input())
counter = Counter()
for i in range(N):
    name = input()
    counter[name] +=1
# print(counter)
books = []
# print(max(counter.values()))
for j in counter.keys():
    if counter[j] == max(counter.values()):
        books.append(j)


books.sort()
print(books[0])