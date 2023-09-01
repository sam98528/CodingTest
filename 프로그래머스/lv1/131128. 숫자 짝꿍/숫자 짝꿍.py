def solution(X, Y):
    answer = ''
    count = dict()
    yCount = dict()
    
    for i in Y:
        if int(i) in yCount:
            yCount[int(i)] += 1
        else:
            yCount[int(i)] = 1
                
    for i in X:
        if int(i) in yCount and yCount[int(i)] > 0:
            yCount[int(i)] -= 1
            if int(i) in count:
                count[int(i)] += 1
            else:
                count[int(i)] = 1
            
    if count:
        for j in range(9,-1,-1):
            if j in count:
                temp = count[j]
                answer += str(j) * temp
        if answer[0] == '0':
            answer = '0'
    else:
        answer = "-1"
        
        
    return answer