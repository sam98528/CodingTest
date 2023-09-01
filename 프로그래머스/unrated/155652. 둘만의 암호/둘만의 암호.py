def solution(s, skip, index):
    answer = ''
    
    for i in range(len(s)):
        temp = index
        tempchar = s[i]
        
        while(temp > 0):
            tempchar = chr(ord(tempchar)+1)
            if ord(tempchar) > 122:
                    tempchar = 'a'
            if tempchar not in skip:
                temp = temp - 1
        answer += tempchar           
    
    print(answer)
    return answer