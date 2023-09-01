def solution(park, routes):
    answer = []
    x, y , xdir, ydir = 0,0,0,0
    check = 0
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == 'S':
                x = row
                y = col
    
    for route in routes:
        check = 0
        dir = route.split()[0]
        steps = int(route.split()[1])
        if dir == 'E':
            if y + steps < len(park[0]):
                for i in range(1,steps+1):
                    if park[x][y+i] == 'X':
                        check = 1
                if check == 0:
                    y += steps
        elif dir =='N':
            if x - steps >= 0: 
                for i in range(1,steps+1):
                    if park[x-i][y] == 'X':
                        check = 1
                if check == 0:
                    x -= steps
        elif dir =='S':
            if x + steps < len(park):
                for i in range(1,steps+1):
                    if park[x+i][y] == 'X':
                        check = 1
                if check == 0:
                    x += steps
        elif dir == 'W':
            if y - steps >= 0 :
                for i in range(1,steps+1):
                    if park[x][y-i] == 'X':
                        check = 1
                if check == 0:
                    y -= steps
            
    answer.append(x)
    answer.append(y)
    return answer