def solution(survey, choices):
    answer = ''
    temp = "RTCFJMAN"
    table = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            table[survey[i][0]] += 4 - choices[i] % 4
        elif choices[i] > 4:
            table[survey[i][1]] += choices[i] % 4
    
    for i in range(0,len(temp)-1,+2):
        if table[temp[i]] < table[temp[i+1]]:
            answer += temp[i+1]
        else:
            answer += temp[i]
        
        
    print(answer)
    return answer