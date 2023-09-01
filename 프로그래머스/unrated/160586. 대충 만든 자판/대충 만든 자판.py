def solution(keymap, targets):
    answer = []
    
    keyDict = dict()
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] in keyDict:
                if keyDict[keymap[i][j]] > j+1:
                    keyDict[keymap[i][j]] = j+1
            else:
                keyDict[keymap[i][j]] = j+1
    
    
    for i in range(len(targets)):
        temp = 0
        for j in range(len(targets[i])):
            if targets[i][j] in keyDict:
                temp += keyDict[targets[i][j]]
            else:
                temp = -1
                break
        answer.append(temp)
    return answer