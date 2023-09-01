def solution(ingredient):
    answer = 0
    order = [1,2,3,1]
    count = 0 
    while count < len(ingredient) - 3:
        if ingredient[count:count+4] == order:
            answer += 1
            del ingredient[count:count+ 4]
            if count < 4:
                count = 0
            else:
                count -= 3
        else:
            count += 1
            
                  
    return answer