def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    
    for word in babbling:
        count = 0
        check = 0
        while count < len(word):
            if word[count] == 'a':
                if word[count : count+3] == can[0]:
                    if word[count+3 : count+6] != can[0]:
                        count += 3
                    else:
                        check = 1
                        break
                else:
                    check = 1
                    break
            elif word[count] == 'y':
                if word[count : count+2] == can[1]:
                    if word[count+2 : count+4] != can[1]:
                        count += 2
                    else:
                        check = 1
                        break
                else:
                    check = 1
                    break
            elif word[count] == 'w':
                if word[count : count+3] == can[2]:
                    if word[count+3 : count+6] != can[2]:
                        count += 3
                    else:
                        check = 1
                        break
                else:
                    check = 1
                    break
            elif word[count] == 'm':
                if word[count : count+2] == can[3]:
                    if word[count+2 : count+4] != can[3]:
                        count += 2
                    else:
                        check = 1
                        break
                else:
                    check = 1
                    break
            else:
                check = 1
                break
                
        if check == 0:
            answer+=1
    return answer