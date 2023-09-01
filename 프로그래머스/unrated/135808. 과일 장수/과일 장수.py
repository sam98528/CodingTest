def solution(k, m, score):
    answer = 0
    score.sort()
    smallest = 0
    if len(score) % m != 0:
        del score[0:len(score)%m]
    
    for i in range(0,len(score)-1,m):
        answer += score[i] * m
            
    print(answer)
    return answer