n, m = map(int, input().split())

x, y, dir = map(int, input().split())

visited = [[0] * m for i in range(n)]
visited[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 1


def turnLeft():
    global dir
    dir -= 1
    if dir < 0:
        dir = 3


turn = 0

while True:
    turnLeft()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        turn += 1
    else:
        if array[nx][ny] != 1 and visited[nx][ny] != 1:
            x = nx
            y = ny
            visited[nx][ny] = 1
            answer += 1
            turn = 0
            continue
        else:
            turn += 1

    if turn == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if array[nx][ny] != 1:
            x = nx
            y = nx
        else:
            break
        turn = 0

print(answer)
