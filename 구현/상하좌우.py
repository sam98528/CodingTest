n = int(input())
paths = input().split()

x, y = 1, 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
pathTemp = ['L', 'R', 'U', 'D']

for path in paths:
    for i in range(len(pathTemp)):
        if path == pathTemp[i]:
            x += dx[i]
            y += dy[i]
            if x > n or x <= 0 or y > n or y <= 0:
                x -= dx[i]
                y -= dy[i]

print(x, y)
