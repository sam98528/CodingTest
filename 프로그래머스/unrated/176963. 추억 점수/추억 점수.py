def solution(name, yearning, photo):
    answer = []
    result = 0
    yearnings = dict()
    for (person,yearns) in zip(name,yearning):
        yearnings[person] = int(yearns)
    
    print(yearnings)
    for listTemp in photo:
        for temp in listTemp:
            if temp in yearnings:
                result += yearnings[temp]
        answer.append(result)
        result = 0
    return answer