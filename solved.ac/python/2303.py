n = int(input())


def dfs(selected, input_list, k, idx):
    global max_idx
    global max_num

    if k ==3 :
        result = 0
        for i in selected:
            result += input_list[i]
        result %= 10

        if result > max_num:
            max_num = result
            max_idx = idx
        elif result == max_num:
            if max_idx < idx:
                max_idx = idx
    else: 
        for i in range(len(input_list)):
            if i not in selected:
                dfs(selected + [i] , input_list, k+1, idx)


card =  [0]
max_num = -1
max_idx = 0
for _ in range(n):
    card.append(list(map(int, input().split())))
for i in range(1, n+1):
    dfs([], card[i], 0, i)
print(max_idx)


