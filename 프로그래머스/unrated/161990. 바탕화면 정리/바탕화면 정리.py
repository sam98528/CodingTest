def solution(wallpaper):
    answer = []
    lux,luy = len(wallpaper),len(wallpaper[0])
    rdx,rdy = 0,0
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == '#':
                if lux > row:
                    lux = row
                if luy > col:
                    luy = col
                if rdx <= row:
                    rdx = row+1
                if rdy <= col:
                    rdy = col+1
                    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    return answer