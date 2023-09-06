from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    answer = 0

    n , m = len(maps),len(maps[0])
    answer = bfs(0,0,maps,n,m)
    return answer

def bfs(x,y,maps,n,m):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    if maps[n-1][m-1] <= 1:
        return -1
    else:
        return(maps[n-1][m-1])


