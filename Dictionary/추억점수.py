def solution(name, yearning, photo):
    answer = []
    result = 0
    yearnings = dict()
    for (person, yearns) in zip(name, yearning):
        yearnings[person] = int(yearns)

    print(yearnings)
    for listTemp in photo:
        for temp in listTemp:
            # Dictionary 사용시 항상 해당 키가 존재하는지 확인해야함.
            if temp in yearnings:
                result += yearnings[temp]
        answer.append(result)
        result = 0
    return answer
