n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
 
grp = []
cnt = 0
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]
 
def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n: # 범위
        return False
    
    if graph[x][y]==1:
        cnt +=1
        graph[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
    
    
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            grp.append(cnt)
            cnt = 0
            
print(len(grp))
grp.sort()
for i in grp:
    print(i)