input = input()
startX, startY = ord(input[0])-ord('A'), int(input[1])-1
print(startX, startY)

answer = 0

steps = [(2, 1), (-2, 1), (2, -1), (-2, -1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in steps:
    xtemp = startX + step[0]
    ytemp = startY + step[1]
    if xtemp > 7 or xtemp < 0 or ytemp > 7 or ytemp < 0:
        continue
    else:
        answer += 1

print(answer)
