def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t)-length+1):
        temp = ""
        for j in range(0,length):
            temp += t[i+j]
        print(temp)
        if int(temp) <= int(p):
            answer += 1
    return answer