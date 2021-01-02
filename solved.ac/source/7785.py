n = int(input())

people = []

for i in range(n):
    name, way = map(str ,input().split())
    if way =="enter":
        people.append(name)
        
    if way =="leave":
        people.remove(name)
    list(set(people))
people = sorted(people)
for i in range(len(people)):
    print(people.pop())
# lst = ["a","c","b"]
# print(sorted(lst).pop())
# 4
# Baha enter
# Askar enter
# Baha leave
# Artem enter