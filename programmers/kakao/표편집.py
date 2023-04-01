def solution(n, k, cmds):
    answer = ''
    nodes = {0: [n-1,1]}
    for i in range(1, n):
        if i == n-1:
            nodes[i] = [i-1, 0]
        else:
            nodes[i] = [i-1, i+1]
    stack = []
    for cmd in cmds:
        if len(cmd) > 1:
            c, x = cmd.split(' ')
            cnt = 0
            if c == 'D':
                while cnt < int(x):
                    k = nodes[k][1]
                    cnt += 1
            else:
                while cnt < int(x):
                    k = nodes[k][0]
                    cnt += 1
        else:
            if cmd == 'C':
                nodes[nodes[k][0]][1] = nodes[k][1]
                nodes[nodes[k][1]][0] = nodes[k][0]
                stack.append([k, nodes[k]])
                tmp = nodes[k]
                del nodes[k]
                if tmp[1] == 0:
                    k = tmp[0]
                else:
                    k = tmp[1]
            else:
                curr_node, val = stack.pop()
                prev_node, next_node = val
                nodes[curr_node] = [prev_node, next_node]
                nodes[prev_node][1] = curr_node
                nodes[next_node][0] = curr_node
    result = ''
    for i in range(n):
        if nodes.get(i) is None:
            result += 'X'
        else:
            result += 'O'


    return result