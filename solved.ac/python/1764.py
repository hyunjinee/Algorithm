N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    name = input()
    a.append(name)
for i in range(M):
    name = input()
    b.append(name)

intersection = list(set(a) & set(b))
p = []
for people in intersection:
    p.append(people)

p.sort()
print(len(p))
for i in p:
    print(i)