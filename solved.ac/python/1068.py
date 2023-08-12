n = int(input())


parents =  list(map(int, input().split()))

del_node = int(input())

tree = {}

for i in range(n):
    if i == del_node or parents[i] == del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)

    else: tree[parents[i]]= [i]

res = 0

print(tree)

if -1 in tree:
    que = [-1]

else: que = []

while que:
    node = que.pop()
    print(node)
    if node not in tree:
        res+= 1

    else:
        que += tree[node]
